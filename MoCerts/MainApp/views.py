import logging
import os
import time

import requests
from datetime import datetime
from allauth.socialaccount.models import SocialAccount

from colorama import Fore, Style

from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.conf import settings
from pyqiwip2p import QiwiP2P

from .names.names_generator import false_user, parse_name
from .certificates.certificate_generator import generate_certificate
from .forms import MyLoginForm, MySignupForm, UserForm, DepositForm, WithdrawalForm
from .models import CustomUser, Certificate, ManualPosts, MainPagePost, QiwiSecretKey, Deposit, Withdrawal
from .tasks import check_payment_status, post_withdrawal_alert  # импорт задачи celery


def get_client_ip(request):
    ip = request.META.get('REMOTE_ADDR')
    return render(request, 'userbalance.html', {'ip_address': ip})


logger = logging.getLogger(__name__)


class AuthorizationForms(FormView):
    """формы для авторизации и регистрации через header"""
    form_class = MyLoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SignupForm'] = MySignupForm
        return context


class MainView(AuthorizationForms, ListView):
    '''Главная страница'''
    model = MainPagePost
    context_object_name = 'posts'
    ordering = ('-date_create')
    template_name = 'MainApp/index.html'


class PostDetail(AuthorizationForms, DetailView):
    '''Страница поста подробнее'''
    model = MainPagePost
    context_object_name = 'post'
    template_name = 'MainApp/postdetail.html'


class UserProfile(LoginRequiredMixin, UpdateView):
    """кабинет пользователя"""
    template_name = 'MainApp/profile.html'
    form_class = UserForm
    success_url = reverse_lazy('profile')
    login_url = '/accounts/login/'

    def get_object(self, **kwargs):
        obj = CustomUser.objects.get(email=self.request.user.email)
        # logger.warning('check')
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = CustomUser.objects.get(email=self.request.user.email)
        return context

    def post(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        messages.add_message(self.request, messages.INFO,
                             'Изменения сохранены')
        return super().post(request, *args, **kwargs)


class ManualView(AuthorizationForms, ListView):
    '''Страница инструкции'''
    model = ManualPosts
    context_object_name = 'manuals'
    template_name = 'MainApp/manual.html'
    ordering = 'index_number'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if not self.request.is_secure():
    #         logger.error(f'self.request.is_secure() {self.request.is_secure()}')
    #     return context


class SelectCertificate(AuthorizationForms, TemplateView):
    """Страница выбора сертификата"""
    template_name = 'MainApp/select_certificate.html'


def cashriser(request):
    users = CustomUser.objects.filter(real_account=True)
    context = {
        'users': users,
    }
    return render(request, 'MainApp/cashriser.html', context)


class CertificateDetail(AuthorizationForms, DetailView):
    model = Certificate
    slug_field = "number"
    slug_url_kwarg = "number"
    context_object_name = 'certificate'
    template_name = 'MainApp/certificate.html'

    def get(self, *args, **kwargs):
        responsive = super().get(*args, **kwargs)
        if self.request.user != self.object.owner:
            '''если сертификат открыл другой польззователь, то отметить как получен'''
            self.object.is_received = True
            self.object.save()
        return responsive

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['host'] = settings.HOST
        if self.object.is_paid == False:
            context['need_pay'] = True
        if self.object.owner == self.request.user:
            context['owner_is_here'] = True
        if self.object.creator == self.request.user:
            context['creator_is_here'] = True
        return context


class MyCertificates(LoginRequiredMixin, ListView):
    '''Страница мои сертификаты'''
    context_object_name = 'queryset'
    template_name = 'MainApp/my_certificates.html'

    def get_queryset(self):
        ''' ===== отсортировать queryset по номиналам в списке 
        а надо по 5шт отсортировать ===== '''
        certificates = Certificate.objects.filter(
            creator=self.request.user, )
        queryset = []
        one_group = []
        for ind, cert in enumerate(certificates):
            if ind % 5 == 0 and ind != 0:
                queryset.append(one_group)
                one_group = []
            one_group.append(cert)
        queryset.append(one_group)

        return queryset


class UserBalance(LoginRequiredMixin, FormView):
    """страница пополнения/вывода баланса"""
    template_name = 'MainApp/userbalance.html'
    success_url = reverse_lazy('profile')
    login_url = '/accounts/login/'
    form_class = DepositForm

    def form_valid(self, form):
        '''Выставить счет на сумму amount рублей который будет работать 15 минут'''
        try:
            # собрать переменные
            amount = form.cleaned_data['amount']
            currency = requests.get(
                'https://www.cbr-xml-daily.ru/daily_json.js').json()['Valute']['USD']['Value']
            # обменять доллары на рубли
            convert_amount = abs(round(currency * amount))
            bill_id = datetime.today().strftime("%d%m%y%H%M%f")
            # bill_id = '0208211659708528'
            email = self.request.user.email
            lifetime = 30
            QIWI_PRIV_KEY = QiwiSecretKey.objects.first().secret_key

            # создать модель транзакции
            Deposit.objects.create(bill_id=bill_id, amount=amount, lifetime=lifetime,
                                   status=1, user=self.request.user)
            # подключиться к сервису qiwi
            p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)
            new_bill = p2p.bill(
                bill_id=bill_id, amount=convert_amount, lifetime=lifetime)
            self.success_url = new_bill.pay_url

            # передать данные для провереи платежа
            check_payment_status.delay(
                QIWI_PRIV_KEY, bill_id, lifetime, email, amount)
            return redirect(self.get_redirect_url())
        except ValueError:
            logger.error('Неверный токен')
            self.success_url = reverse('errorview')
            return redirect(self.get_redirect_url())
        except AttributeError:
            logger.error('Создайте токен qiwi')
            self.success_url = reverse('errorview')
            return redirect(self.get_redirect_url())

    def get_redirect_url(self):
        return self.success_url

    def bSort(array):
        # определяем длину массива
        length = len(array)
        # Внешний цикл, количество проходов N-1
        for i in range(length):
            # Внутренний цикл, N-i-1 проходов
            for j in range(0, length - i - 1):
                # Меняем элементы местами
                if array[j.time] > array[j.time + 1]:
                    temp = array[j]
                    array[j.time] = array[j.time + 1]
                    array[j + 1] = temp
        return array

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['WithdrawalForm'] = WithdrawalForm
        deposit = Deposit.objects.filter(
            user=self.request.user).order_by('-id')
        withdrawal = Withdrawal.objects.filter(
            user=self.request.user).order_by('-id')
        transactions = []
        for i in deposit:
            transactions.append(i)
        for i in withdrawal:
            transactions.append(i)
        # transactions = self.bSort(transactions)
        context['transactions'] = transactions
        return context

    def get(self, request: HttpRequest, *args: str, **kwargs) -> HttpResponse:
        '''вывод средств'''
        if request.GET.get('withdrawal_amount'):
            withdrawal_amount = request.GET.get('withdrawal_amount')
            user = self.request.user
            if int(withdrawal_amount) > 0 and int(withdrawal_amount) <= user.balance:
                withdrawal_amount = request.GET.get('withdrawal_amount')
                qiwi_wallet = request.GET.get('qiwi_wallet')
                bill_id = datetime.today().strftime("%d%m%y%H%M%f")
                transaction = Withdrawal.objects.create(bill_id=bill_id, user=user,
                                                        amount=withdrawal_amount, qiwi_wallet=qiwi_wallet, status=1, )
                link = transaction.get_absolute_url()
                user.balance = user.balance - int(withdrawal_amount)
                user.save()
                post_withdrawal_alert.delay(
                    user.email, withdrawal_amount, link)
                messages.add_message(self.request, messages.INFO, 'Ваша заявка на вывод средств\
                     принята, скоро ваша заявка будет обработана')
                return HttpResponseRedirect(reverse('userbalance'))
            else:
                messages.add_message(
                    self.request, messages.INFO, 'Форма заполнена неверно')
        return super().get(request, *args, **kwargs)


class ErrorView(TemplateView):
    '''сервис не доступен'''
    template_name = 'MainApp/service_error.html'


#
def create_user():
    pass


@login_required
def create_certificate(request, nominal):
    ''' ==== Создать сертификат ===== '''
    if request.method == 'GET':
        user = request.user
        if Certificate.objects.filter(owner=user, nominal=nominal, is_paid=False).exists():
            return HttpResponseRedirect(reverse('certificate',
                                                kwargs={'number': Certificate.objects.get(owner=user, nominal=nominal,
                                                                                          is_paid=False)}))

        number = datetime.today().strftime("%d%m%y%H%M%f")
        url = '{}/certificate/{}'.format(settings.HOST, number)

        user1_fullname = false_user()
        user2_fullname = false_user()
        user3_fullname = false_user()

        user1 = CustomUser.objects.create(username=user1_fullname[0] + user2_fullname[1], first_name=user1_fullname[0],
                                          last_name=user1_fullname[1],
                                          email=f'fakeuser1{number}@gmail.com',
                                          password=user2_fullname, real_account=False, )
        user2 = CustomUser.objects.create(username=user2_fullname[0] + user3_fullname[1], first_name=user2_fullname[0],
                                          last_name=user2_fullname[1],
                                          email=f'fakeuser2{number}@gmail.com',
                                          password=user3_fullname, real_account=False, )
        user3 = CustomUser.objects.create(username=user1_fullname[0] + user3_fullname[1], first_name=user3_fullname[0],
                                          last_name=user3_fullname[1],
                                          email=f'fakeuser3{number}@gmail.com',
                                          password=user1_fullname, real_account=False, )
        image_certificate = generate_certificate(
            nominal, number, user1, user2, user3)
        certificate = Certificate(number=number, url=url, nominal=nominal, user1=user1, user2=user2, user3=user3,
                                  certificate_image=image_certificate, owner=request.user, )
        certificate.save()
        user.certificate = certificate
        user.save()
        return HttpResponseRedirect(reverse('certificate',
                                            kwargs={'number': request.user.certificate.number}))


@login_required
def pay_certificate(request, pk):
    '''оплата сертификата'''
    certificate = Certificate.objects.get(id=pk)
    if request.user.balance >= certificate.nominal:
        certificate.owner = request.user
        certificate.is_paid = True
        certificate.paid_by_user = request.user
        certificate.save()

        request.user.balance -= certificate.nominal
        request.user.save()

        user1 = certificate.user1
        if user1.real_account:
            user1.balance += certificate.nominal
            user1.save()
        else:
            if CustomUser.objects.filter(email=settings.MONEY_ADMIN['email']).exists():
                money_admin = CustomUser.objects.get(
                    email=settings.MONEY_ADMIN['email'])
            else:
                money_admin = CustomUser.objects.create(username=settings.MONEY_ADMIN['username'],
                                                        first_name=settings.MONEY_ADMIN['first_name'],
                                                        last_name=settings.MONEY_ADMIN['last_name'],
                                                        email=settings.MONEY_ADMIN['email'],
                                                        password=settings.MONEY_ADMIN['password'], )
            money_admin.balance += certificate.nominal
            money_admin.save()

        for i in range(0, 5):
            user1, user2, user3 = certificate.user2, certificate.user3, request.user
            number = datetime.today().strftime("%d%m%y%H%M%f")
            image_certificate = generate_certificate(
                certificate.nominal, number, user1, user2, user3)
            url = '{}/certificate/{}'.format(settings.HOST, number)

            new_certificate = Certificate(number=number, url=url, nominal=certificate.nominal, user1=user1,
                                          user2=user2, user3=user3, certificate_image=image_certificate,
                                          creator=request.user, owner=request.user, )
            new_certificate.save()

        return HttpResponseRedirect(reverse('my_certificates'))
    else:
        messages.add_message(
            request, messages.ERROR, 'Недостаточно средств, пожалуйста, пополните баланс')
    return HttpResponseRedirect(reverse('userbalance'))


@login_required
def accept(request, pk):
    '''Подтвердить сертификат'''
    certificate = Certificate.objects.get(pk=pk)
    certificate.owner = request.user
    certificate.save()
    request.user.certificate = certificate
    request.user.save()
    return HttpResponseRedirect(reverse('certificate',
                                        kwargs={'number': certificate.number}))


def generate(request):
    """ ===== Генератор ===== """
    if request.method == "POST":
        count_certificates = request.POST.get('count_certificate')
        number = int(count_certificates)
        user = request.POST.get('choose_user')
        nominal = request.POST.get('nominal')

        if number > 0 and number != '':
            while number > 0:
                number_certificate = datetime.today().strftime("%d%m%y%H%M%f")
                url = '{}/certificate/{}'.format(settings.HOST, number_certificate)
                user1_fullname = false_user()
                user2_fullname = false_user()
                user3_fullname = false_user()

                user1 = CustomUser.objects.create(username=user1_fullname[0] + user2_fullname[1],
                                                  first_name=user1_fullname[0],
                                                  last_name=user1_fullname[1],
                                                  email=f'fakeuser1{number}@gmail.com',
                                                  password=user2_fullname, real_account=False, )
                user2 = CustomUser.objects.create(username=user2_fullname[0] + user3_fullname[1],
                                                  first_name=user2_fullname[0],
                                                  last_name=user2_fullname[1],
                                                  email=f'fakeuser2{number}@gmail.com',
                                                  password=user3_fullname, real_account=False, )
                if user is None:
                    user3 = CustomUser.objects.create(username=user1_fullname[0] + user3_fullname[1], first_name=user3_fullname[0],
                                          last_name=user3_fullname[1],
                                          email=f'fakeuser3{number}@gmail.com',
                                          password=user1_fullname, real_account=False, )
                else:
                    parse_names = parse_name(user)
                    user3 = CustomUser.objects.get(first_name=parse_names[0], last_name=parse_names[1],
                                                    email=parse_names[2])

                image_certificate = generate_certificate(nominal, number_certificate, user1, user2, user3)

                Certificate.objects.create(number=number_certificate, url=url, nominal=nominal,
                                               user1=user1, user2=user2, user3=user3,
                                               certificate_image=image_certificate, owner=request.user)

                number -= 1
        certificates = Certificate.objects.all().order_by('-pk')[:int(count_certificates)]
        context = {
            'certificates': certificates,
        }
        return render(request, 'MainApp/cashriser.html', context)

    return render(request, 'MainApp/cashriser.html')





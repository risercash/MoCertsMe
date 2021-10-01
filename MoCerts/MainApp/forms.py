from allauth.account.forms import LoginForm, SignupForm
from django import forms
from django.forms import ModelForm, TextInput, CharField, EmailInput, IntegerField, NumberInput, Select
from django.forms.fields import ChoiceField
from django.core.validators import MinValueValidator
from django.forms.widgets import Textarea

from .models import CustomUser, SendUs


class DepositForm(forms.Form):
    '''форма пополнения.'''
    VAL_CHOICES = (
        ("USD", 'USD Доллар'),
        ("EUR", 'EUR Евро'),
        ("RUB", 'RUB Рубль'),
        ("KZT", 'KZT Тенге'),
    )
    amount = IntegerField(label='Сумма пополнения', widget=NumberInput(attrs={'placeholder': 'сумма'}),
                          validators=[MinValueValidator(1), ])
    valute = ChoiceField(label='Валюта', choices=VAL_CHOICES, initial="USD")

    def __init__(self, *args, **kwargs):
        super(DepositForm, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs['min'] = 1


class WithdrawalForm(forms.Form):
    '''форма вывода средств'''

    withdrawal_amount = IntegerField(label='Сумма вывода', widget=NumberInput(attrs={'placeholder': 'сумма вывода'}),
                                     validators=[MinValueValidator(1), ])
    qiwi_wallet = CharField(
        label='Qiwi кошелек', widget=TextInput(attrs={'placeholder': 'или номер карты'}), required=True)

    def __init__(self, *args, **kwargs):
        super(WithdrawalForm, self).__init__(*args, **kwargs)
        self.fields['withdrawal_amount'].widget.attrs['min'] = 1


class PrepaidCerts(forms.Form):
    """Форма предоплаченных сертификатов."""
    CERT_TYPE = (
        ("regular", 'Обычный'),
        ("custom", 'Именной'),
    )
    NOMINALS = (("1", '1'), ("5", '5'), ("10", '10'), ("20", '20'),
                ("50", '50'), ("100", '100'), ("200", '200'), ("500", '500'),)

    type = ChoiceField(choices=CERT_TYPE, initial="regular",
                       widget=Select(attrs={'placeholder': 'Тип сертификата'}))
    nominal = ChoiceField(choices=NOMINALS, initial="regular", widget=Select(
        attrs={'placeholder': 'Тип сертификата'}))
    amount = IntegerField(label='Количество', widget=NumberInput(attrs={'placeholder': 'Количество'}),
                          validators=[MinValueValidator(1), ], required=True, initial=1)
    user = CharField(max_length=50, required=False,
                     widget=TextInput(attrs={'placeholder': 'email'}))

    def __init__(self, *args, **kwargs):
        super(PrepaidCerts, self).__init__(*args, **kwargs)
        self.fields['amount'].widget.attrs['min'] = 1


class SendUsForm(forms.ModelForm):
    """Форма обратной связи."""
    class Meta:
        model = SendUs
        fields = ['username', 'email', 'text',]

        widgets = {
            'username': TextInput(attrs={'placeholder' : 'Имя Фамилия'}), 
            'email': TextInput(attrs={'placeholder' : 'Email или Telegram'}), 
            'text': Textarea(attrs={'placeholder' : 'Сообщение...'}), 
            }


class MyLoginForm(LoginForm):
    """Логин."""
    def save(self, request):
        user = super(MyLoginForm, self).save(request)
        return user


class MySignupForm(SignupForm, ModelForm):
    """Форма обратной связи."""
    first_name = CharField(
        label='Имя', widget=TextInput(attrs={'placeholder': 'Имя'}), required=True)
    last_name = CharField(
        label='Имя', widget=TextInput(attrs={'placeholder': 'Фамилия'}), required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', ]

    def save(self, request):
        user = super(MySignupForm, self).save(request)
        return user


class UserForm(ModelForm):
    """Модельная форма редактировать профиль"""

    class Meta:
        model = CustomUser

        fields = ['photo', 'first_name', 'last_name', 'email', 'phone']

        labels = {'first_name': 'Имя',
                  'last_name': 'Фамилия', 'email': 'Email', 'photo': 'Аватар', 'phone': '87003002010'}

        widgets = {'email': EmailInput(), }
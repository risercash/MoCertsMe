from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from embed_video.fields import EmbedVideoField
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError

from MoCerts.settings import HOST


class CustomUser(AbstractUser):
    ''''расширение модели пользователя'''
    photo = models.FileField(upload_to='avatars', blank=True,
                             verbose_name='Аватарка', default='def/default-user-image.png')
    certificate = models.ForeignKey(
        'Certificate', on_delete=models.SET_NULL, null=True, blank=True)
    telegram_id = models.BigIntegerField(
        verbose_name='telegram id', blank=True, default=0)
    phone = models.CharField(max_length=12,
                             verbose_name='phone number', blank=True, default=0)
    address = models.CharField(max_length=255,
                               verbose_name='address', blank=True, default=0)
    balance = models.PositiveIntegerField(verbose_name='balance', default=0)
    real_account = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        '''Строковое отображение'''
        return f'{self.first_name}'

    def get_absolute_url(self):
        """получить ссылку на объект"""
        return reverse('profile')


class Certificate(models.Model):
    '''модель сертификата'''
    number = models.BigIntegerField(verbose_name='Номер сертификата')
    url = models.URLField(max_length=255, verbose_name='Ссылка на сертификат')
    nominal = models.IntegerField(verbose_name='Номинал', default=1)
    user1 = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name='first_users')
    user2 = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name='second_users')
    user3 = models.ForeignKey(
        CustomUser, on_delete=models.PROTECT, related_name='third_users')
    published_date = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    certificate_image = models.ImageField(
        upload_to='certificates/image/%Y/%m/%d', blank=True, verbose_name='Рисунок')
    creator = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=None, null=True, blank=True,
                                related_name='made_by_user')
    owner = models.ForeignKey(CustomUser, on_delete=models.PROTECT, default=None, null=True, blank=True,
                              related_name='owner')
    is_paid = models.BooleanField(default=False)
    is_received = models.BooleanField(default=False)
    paid_by_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, default=None, null=True, blank=True,
                                     related_name='paid_by_user')
    is_prepaid = models.BooleanField(default=False)
    named_after = models.BooleanField(default=False)
    

    def get_url_for_messengers(self):
        """получить ссылку на объект"""
        return f"{HOST + str(reverse('certificate', kwargs={'number': self.number}))}"

    class Meta:
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def __str__(self):
        '''Строковое отображение'''
        return f'{self.number}'

    def get_absolute_url(self):
        """получить ссылку на объект"""
        return reverse('certificate', kwargs={'number': self.number})


class PreviewSettings(models.Model):
    '''модель настройки превью страниц'''
    type = models.CharField(
        max_length=255, default='website', verbose_name='Тип приложения',)
    site_name = models.CharField(
        max_length=255, default='MoCert', verbose_name='Название сайта',)
    title = models.CharField(
        max_length=255, default='Заработай вместе с нами', verbose_name='Заголовок',)
    description = models.CharField(max_length=255, default='Перейди по ссылке и получи сертификат',
                                   verbose_name='Описание',)
    locale = models.CharField(
        max_length=255, default='ru', verbose_name='Локаль',)
    twitter_creator = models.CharField(
        max_length=255, default='@MonteCarlo', verbose_name='twitter_creator',)
    url = models.URLField(max_length=255, default=HOST, verbose_name='Ссылка на сайт',
                          help_text='Данное поле для всех страниц. Для сертификатов подставляется свой url')
    image = models.URLField(max_length=255, default=HOST + '/media/preview.jpg', verbose_name='Ссылка на картинку',
                            help_text='Данное поле для всех страниц. Для сертификатов подставляется своя картинка',)

    class Meta:
        verbose_name = 'Настройки превью'
        verbose_name_plural = 'Настройки превью'

    def __str__(self):
        '''Строковое отображени'''
        return f'{self.site_name}'


class ManualPosts(models.Model):
    index_number = models.PositiveIntegerField(
        verbose_name='порядковый номер на странице',)
    title = models.CharField(max_length=255, blank=True,
                             verbose_name='Заголовок',)
    description = models.CharField(
        max_length=255, blank=True, verbose_name='Описание')
    # video = EmbedVideoField(blank=True, verbose_name='Ссылка на видео')
    video = models.TextField(blank=True, verbose_name='Iframe код видео',
                             help_text='Вставьте только iframe код видео файла, обычная ссылка не допустима')

    class Meta:
        verbose_name = 'Инструкция'
        verbose_name_plural = 'Инструкции'

    def __str__(self):
        '''Строковое отображение'''
        return f'{self.title}'

    def get_absolute_url(self):
        """получить ссылку на объект"""
        return reverse('manual',)

    def clean(self):
        iframe = self.video
        if iframe.find('iframe') == -1:
            raise ValidationError(
                {'video': "Вставьте только iframe код видео файла, обычная ссылка не допустима"})
        index = self.index_number
        if ManualPosts.objects.filter(index_number=index).exists():
            if ManualPosts.objects.get(index_number=index).id != self.id:
                raise ValidationError(
                    {'index_number': "Порядковый номер с таким значением уже существует, выберите другой"})


class MainPagePost(models.Model):
    headline = models.CharField(max_length=90, null=False, verbose_name=pgettext_lazy('Заголовок', 'Заголовок'),
                                help_text='максимум 50 символов')
    subtitle = models.CharField(max_length=150, null=False,
                                verbose_name=pgettext_lazy('Подзаголовок', 'Подзаголовок'))
    date_create = models.DateTimeField(auto_now_add=True, verbose_name=pgettext_lazy(
        'Дата публикации', 'Дата публикации'))
    content = RichTextUploadingField(
        blank=True, null=True, verbose_name=pgettext_lazy('Содержание', 'Содержание'))
    photo = models.FileField(upload_to='posts', blank=True,
                             verbose_name='PostPhoto', default='def/default-user-image.png')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        '''Строковое отображение'''
        return f'{self.headline}'

    def get_absolute_url(self):
        """получить ссылку на объект"""
        return reverse('postdetail', kwargs={'pk': self.id})


class QiwiSecretKey(models.Model):
    '''модель QiwiToken'''
    secret_key = models.CharField(
        max_length=255, default='Token', verbose_name=pgettext_lazy('secret_key', 'secret_key'))

    def save(self, *args, **kwargs):
        '''модель может быть только в единственном экземпляре'''
        if not self.pk and QiwiSecretKey.objects.exists():
            raise ValidationError(
                'There is can be only one QiwiSecretKey instance')
        return super(QiwiSecretKey, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Токен qiwi'
        verbose_name_plural = 'Токен qiwi'

    def __str__(self):
        '''Строковое отображение'''
        return f'{self.secret_key}'


class Deposit(models.Model):
    '''модель транзакции для пополнения'''

    class StatusList(models.IntegerChoices):
        WAIT = 1, _('В ожидании')
        PAID = 2, _('Оплачено')
        EXPIRED = 3, _('Истекший')
        REJECT = 4, _('Отклонено')

    bill_id = models.PositiveBigIntegerField(
        unique=True, verbose_name=pgettext_lazy('id транзакции', 'id транзакции'),)
    amount = models.PositiveIntegerField(
        verbose_name=pgettext_lazy('сумма, руб', 'сумма, руб'),)
    status = models.PositiveIntegerField(
        choices=StatusList.choices, default=StatusList.WAIT)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, default=None, null=True, blank=True,
                             related_name='deposit_by_user')
    time = models.DateField(auto_now_add=True, verbose_name='время создания',)
    type = models.CharField(max_length=255, default='Пополнение',
                            verbose_name=pgettext_lazy('тип транзакции', 'тип транзакции'),)
    lifetime = models.PositiveIntegerField(verbose_name=pgettext_lazy(
        'время жизни счета, мин', 'время жизни счета, мин'),)

    class Meta:
        verbose_name = 'Пополнение'
        verbose_name_plural = 'Пополнения'

    def __str__(self):
        '''Строковое отображение'''
        return f'{self.time}'

    def get_absolute_url(self):
        """получить ссылку на объект"""
        return reverse('userbalance')


class Withdrawal(models.Model):
    '''модель транзакции для вывода средств'''

    class StatusList(models.IntegerChoices):
        WAIT = 1, _('В процессе')
        PAID = 2, _('Исполнено')
        REJECT = 3, _('Отклонено')

    bill_id = models.CharField(unique=True, max_length=255, verbose_name=pgettext_lazy(
        'id транзакции', 'id транзакции'),)
    amount = models.PositiveIntegerField(
        verbose_name=pgettext_lazy('сумма', 'сумма'),)
    status = models.PositiveIntegerField(
        choices=StatusList.choices, default=StatusList.WAIT)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, default=None, null=True, blank=True,
                             related_name='withdrawal_by_user')
    time = models.DateField(auto_now_add=True, verbose_name='время создания',)
    type = models.CharField(max_length=255, default='Вывод средств',
                            verbose_name=pgettext_lazy('тип транзакции', 'тип транзакции'),)
    qiwi_wallet = models.CharField(max_length=255, verbose_name=pgettext_lazy(
        'номер кошелька', 'номер кошелька'),)

    class Meta:
        verbose_name = 'Вывод средств'
        verbose_name_plural = 'Вывод средств'

    def __str__(self):
        '''Строковое отображение'''
        return f'{self.user} - {self.bill_id}'

    def get_absolute_url(self):
        """получить ссылку на объект"""
        return HOST + '/nimda/MainApp/withdrawal/'


class SendUs(models.Model):
    '''модель для запросов обратной связи'''
    username = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    text = models.TextField(blank=False)
    date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        '''Строковое отображение'''
        return f'{self.username} - {self.email}'

    def get_absolute_url(self):
        """получить ссылку на объект"""
        return reverse('send_us')
from django.db.models.signals import post_delete, pre_delete, post_save
from allauth.account.signals import user_signed_up
from django.db.models import ProtectedError
from django.dispatch import receiver
from .models import Certificate, Withdrawal, CustomUser
from django.conf import settings
from .tasks import welcome_email
import logging
import os


logger = logging.getLogger(__name__)


@receiver(post_delete, sender=Certificate)
def delete_certificate_picture(sender, instance, **kwargs):
    '''При удалении сертификата, так же удалить его картинку'''
    logger.warning('Certificate was deleted ' + str(instance))
    try:  # удаление картинку
        crop_picture_path = os.path.join(settings.MEDIA_DIR, str(
            instance.certificate_image) + '.182x129_q85_crop-smart.png')
        print(crop_picture_path)
        os.remove(crop_picture_path)
        picture_path = os.path.join(
            settings.MEDIA_DIR, str(instance.certificate_image))
        os.remove(picture_path)
    except FileNotFoundError:
        picture_path = os.path.join(
            settings.MEDIA_DIR, str(instance.certificate_image))
        os.remove(picture_path)


@receiver(post_delete, sender=Certificate)
def delete_fake_user(sender, instance, **kwargs):
    '''При удалении сертификата, так же удалить его фейк юзеров.'''
    try:
        def delete_fake_user(user):
            if not user.real_account:
                if Certificate.objects.filter(user1=user).count() <= 0 \
                    and Certificate.objects.filter(user2=user).count() <= 0 \
                        and Certificate.objects.filter(user2=user).count() <= 0:
                    print(CustomUser.objects.get(id=user.id))
                    CustomUser.objects.get(id=user.id).delete()

        delete_fake_user(instance.user1)
        delete_fake_user(instance.user2)
        delete_fake_user(instance.user3)
    except:
        pass


@receiver(post_save, sender=Withdrawal)
def my_handler(sender, instance, **kwargs):
    '''При отклонении вывода, обратно вернуть средства пользователю'''
    if instance.status == 3:
        user = CustomUser.objects.get(id=instance.user.id)
        user.balance += instance.amount
        user.save()


@receiver(user_signed_up, dispatch_uid="some.unique.string.id.for.allauth.user_signed_up")
def user_signed_up_(request, user, **kwargs):
    '''Отправить приветстенное письмо, после регистрации'''
    welcome_email.delay(user.username, user.email)

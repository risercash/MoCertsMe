from django.db.models.signals import pre_delete
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from .models import Certificate
from django.conf import settings
from .tasks import welcome_email
import logging
import os


logger = logging.getLogger(__name__)


@receiver(pre_delete, sender=Certificate)
def delete_certificate_picture(sender, instance, **kwargs):
    '''При удалении сертификата, так же удалить его картинку'''
    logger.info('Certificate was deleted ' + str(instance))
    try:
        crop_picture_path = os.path.join(settings.MEDIA_DIR, str(instance.certificate_image) + '.182x129_q85_crop-smart.png')
        print(crop_picture_path)
        os.remove(crop_picture_path)
        picture_path = os.path.join(settings.MEDIA_DIR, str(instance.certificate_image))
        os.remove(picture_path)
    except FileNotFoundError:
        picture_path = os.path.join(settings.MEDIA_DIR, str(instance.certificate_image))
        os.remove(picture_path)


@receiver(user_signed_up, dispatch_uid="some.unique.string.id.for.allauth.user_signed_up")
def user_signed_up_(request, user, **kwargs):
    '''Отправить приветстенное письмо, после регистрации'''
    print('User sign up2!', (user))
    welcome_email.delay(user.username, user.email)
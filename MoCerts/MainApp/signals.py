from django.db.models.signals import pre_delete
from django.dispatch import receiver
from .models import Certificate
from django.conf import settings
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
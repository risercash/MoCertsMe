from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
import os


def generate_certificate(nominal, number, user1, user2, user3):
    ''' ===== Генератор нового сертификата ===== '''
    first_user = f'1. {user1.first_name} {user1.last_name}'
    second_user = f'2. {user2.first_name} {user2.last_name}'
    third_user = f'3. {user3.first_name} {user3.last_name}'
    number_text = str(number)
    init_image_name = f'cert_big_{nominal}.png'
    image_path = os.path.join(settings.MEDIA_DIR, init_image_name)
    font_path = os.path.join(settings.MEDIA_DIR + 'fonts/', 'font.ttf')
    font_path_number = os.path.join(settings.MEDIA_DIR + 'fonts/', 'georgia.ttf')
    img = Image.open(image_path)
    font = ImageFont.truetype(font_path, size=26)
    draw_text = ImageDraw.Draw(img)
    draw_text.text((24, 180), first_user, font=font)
    draw_text.text((41, 214), second_user, font=font)
    draw_text.text((62, 248), third_user, font=font)
    font_number = ImageFont.truetype(font_path_number, size=18)
    draw_text.text((260, 367), number_text, font=font_number, fill='black', stroke_width=1)
    file_name_result = f'certificates/{number}.png'
    file_name_result_path = os.path.join(settings.MEDIA_DIR, file_name_result)
    try:
        img.save(file_name_result_path)
    except FileNotFoundError:
        directory_path = os.path.join(settings.MEDIA_DIR, 'certificates')
        os.makedirs(directory_path,exist_ok=True)
        img.save(file_name_result_path)
    return file_name_result
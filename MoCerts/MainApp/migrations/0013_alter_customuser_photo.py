# Generated by Django 3.2.5 on 2021-08-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0012_alter_customuser_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.FileField(blank=True, upload_to='avatars', verbose_name='Аватарка'),
        ),
    ]

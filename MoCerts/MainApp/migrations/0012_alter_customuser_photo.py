# Generated by Django 3.2.5 on 2021-08-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0011_auto_20210805_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=models.ImageField(blank=True, upload_to='board/image/%Y/%m', verbose_name='Аватарка'),
        ),
    ]

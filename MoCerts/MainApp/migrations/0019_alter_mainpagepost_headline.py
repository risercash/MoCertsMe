# Generated by Django 3.2.5 on 2021-08-25 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0018_alter_mainpagepost_headline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainpagepost',
            name='headline',
            field=models.CharField(help_text='максимум 50 символов', max_length=90, verbose_name='Заголовок'),
        ),
    ]
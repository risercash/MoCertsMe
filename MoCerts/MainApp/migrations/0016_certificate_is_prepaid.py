# Generated by Django 3.2.5 on 2021-08-24 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0015_auto_20210821_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='is_prepaid',
            field=models.BooleanField(default=False),
        ),
    ]

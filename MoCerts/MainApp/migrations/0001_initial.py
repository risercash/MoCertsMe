# Generated by Django 3.2.5 on 2021-09-04 10:13

import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.BigIntegerField(verbose_name='Номер сертификата')),
                ('url', models.URLField(max_length=255, verbose_name='Ссылка на сертификат')),
                ('nominal', models.IntegerField(default=1, verbose_name='Номинал')),
                ('published_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')),
                ('certificate_image', models.ImageField(blank=True, upload_to='certificates/image/%Y/%m/%d', verbose_name='Рисунок')),
                ('is_paid', models.BooleanField(default=False)),
                ('is_prepaid', models.BooleanField(default=False)),
                ('is_accept', models.BooleanField(default=True)),
                ('is_received', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Сертификат',
                'verbose_name_plural': 'Сертификаты',
            },
        ),
        migrations.CreateModel(
            name='MainPagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(help_text='максимум 50 символов', max_length=90, verbose_name='Заголовок')),
                ('subtitle', models.CharField(max_length=150, verbose_name='Подзаголовок')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Содержание')),
                ('photo', models.FileField(blank=True, default='def/default-user-image.png', upload_to='posts', verbose_name='PostPhoto')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='ManualPosts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_number', models.PositiveIntegerField(verbose_name='порядковый номер на странице')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'Инструкцию',
                'verbose_name_plural': 'Инструкции',
            },
        ),
        migrations.CreateModel(
            name='PreviewSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='website', max_length=255, verbose_name='Тип приложения')),
                ('site_name', models.CharField(default='MoCert', max_length=255, verbose_name='Название сайта')),
                ('title', models.CharField(default='Заработай вместе с нами', max_length=255, verbose_name='Заголовок')),
                ('description', models.CharField(default='Перейди по ссылке и получи сертификат', max_length=255, verbose_name='Описание')),
                ('locale', models.CharField(default='ru', max_length=255, verbose_name='Локаль')),
                ('twitter_creator', models.CharField(default='@MonteCarlo', max_length=255, verbose_name='twitter_creator')),
                ('url', models.URLField(default='127.0.0.1', help_text='Данное поле для всех страниц. Для сертификатов подставляется свой url', max_length=255, verbose_name='Ссылка на сайт')),
                ('image', models.URLField(default='127.0.0.1/media/2607211245970578.png', help_text='Данное поле для всех страниц. Для сертификатов подставляется своя картинка', max_length=255, verbose_name='Ссылка на картинку')),
            ],
            options={
                'verbose_name': 'Настройки превью',
                'verbose_name_plural': 'Настройки превью',
            },
        ),
        migrations.CreateModel(
            name='QiwiSecretKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_key', models.CharField(default='Token', max_length=255, verbose_name='secret_key')),
            ],
            options={
                'verbose_name': 'Токен qiwi',
                'verbose_name_plural': 'Токен qiwi',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('photo', models.FileField(blank=True, default='def/default-user-image.png', upload_to='avatars', verbose_name='Аватарка')),
                ('telegram_id', models.BigIntegerField(blank=True, default=0, verbose_name='telegram id')),
                ('balance', models.PositiveIntegerField(default=0, verbose_name='balance')),
                ('real_account', models.BooleanField(default=True)),
                ('certificate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='MainApp.certificate')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.CharField(max_length=255, unique=True, verbose_name='id транзакции')),
                ('amount', models.PositiveIntegerField(verbose_name='сумма')),
                ('status', models.PositiveIntegerField(choices=[(1, 'В процессе'), (2, 'Исполнено'), (3, 'Отклонено')], default=1)),
                ('time', models.DateField(auto_now_add=True, verbose_name='время создания')),
                ('type', models.CharField(default='Вывод средств', max_length=255, verbose_name='тип транзакции')),
                ('qiwi_wallet', models.CharField(max_length=255, verbose_name='номер кошелька')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='withdrawal_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Вывод средств',
                'verbose_name_plural': 'Вывод средств',
            },
        ),
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_id', models.PositiveBigIntegerField(unique=True, verbose_name='id транзакции')),
                ('amount', models.PositiveIntegerField(verbose_name='сумма, руб')),
                ('status', models.PositiveIntegerField(choices=[(1, 'В ожидании'), (2, 'Оплачено'), (3, 'Истекший'), (4, 'Отклонено')], default=1)),
                ('time', models.DateField(auto_now_add=True, verbose_name='время создания')),
                ('type', models.CharField(default='Пополнение', max_length=255, verbose_name='тип транзакции')),
                ('lifetime', models.PositiveIntegerField(verbose_name='время жизни счета, мин')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deposit_by_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пополнение',
                'verbose_name_plural': 'Пополнения',
            },
        ),
        migrations.AddField(
            model_name='certificate',
            name='made_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='made_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='certificate',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='certificate',
            name='paid_by_user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paid_by_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='certificate',
            name='user1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='first_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='certificate',
            name='user2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='second_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='certificate',
            name='user3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='third_users', to=settings.AUTH_USER_MODEL),
        ),
    ]

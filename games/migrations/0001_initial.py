# Generated by Django 5.2 on 2025-04-18 13:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('launch_date', models.DateField(verbose_name='زمان راه اندازی')),
                ('price', models.IntegerField(default=0, verbose_name='قیمت')),
                ('rating', models.IntegerField(verbose_name='امتیاز بازی')),
                ('stars', models.IntegerField(verbose_name='تعداد ستاره ها')),
                ('download_link', models.CharField(help_text='اکر لینک در اینجا قرار نگرفت ازابزار های کوتاه کننده ی لینک استفاده کنید', max_length=255, verbose_name='لینک دانلود')),
                ('media', models.FileField(upload_to='Games/media/', verbose_name='رسانه')),
                ('description', models.TextField(verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'بازی',
                'verbose_name_plural': 'بازی ها',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='نام  بازیکن')),
                ('image', models.ImageField(upload_to='TeamMembers/member_images/', verbose_name='تصویر بازیکن')),
                ('skill', models.CharField(choices=[('بازیکن تازه کار', 'Rookie player'), ('بازیکن متوسط ', 'Average player'), ('بازیکن حرفه ای', 'Professional player')], default='یازیکن تازه کار', max_length=50, verbose_name='سطح مهارت')),
            ],
            options={
                'verbose_name': 'عضو تیم',
                'verbose_name_plural': 'اعضای تیم',
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('tournament_date', models.DateField(verbose_name='زمان مسابقه')),
                ('image', models.ImageField(upload_to='Tournaments/%Y/%m/%d', verbose_name='تصویر مسابقه')),
                ('video', models.FileField(upload_to='Tournaments/videos/', verbose_name='ویدیو مسابقه')),
            ],
            options={
                'verbose_name': 'مسابقه',
                'verbose_name_plural': 'مسابقات',
            },
        ),
        migrations.CreateModel(
            name='UpcomingGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('release_date', models.DateField(verbose_name='زمان عرضه')),
                ('icon', models.ImageField(upload_to='Games/icon/', verbose_name='آیکون')),
            ],
            options={
                'verbose_name': 'بازی در حال انتشار',
                'verbose_name_plural': 'بازیهای در حال انتشار',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(choices=[('کاربر عادی', 'Normal user'), ('وبلاگ\u200cنویس', 'Blogger'), ('منتقد بازی', 'Game Critic'), ('توسعه\u200cدهنده بازی', 'Game Developer'), ('استریمر', 'Streamer'), ('طراح بازی', 'Game Designer'), ('بازیکن حرفه\u200cای', 'Pro Gamer')], default='کاربر عادی', max_length=50, verbose_name='نقش کاربر')),
                ('text', models.TextField(verbose_name='متن نظر')),
                ('avatar', models.ImageField(upload_to='Games/avatrs/', verbose_name='آواتار')),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='نام کاربر')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game', verbose_name='نظرات بازی')),
            ],
            options={
                'verbose_name': 'نظر',
                'verbose_name_plural': 'نظرات',
            },
        ),
        migrations.CreateModel(
            name='GameNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان خبر بازی')),
                ('description', models.TextField(verbose_name='متن خبر')),
                ('image', models.ImageField(upload_to='GameNews/%Y/%m/%d', verbose_name='تصویر خبر')),
                ('publish_date', models.DateField(auto_now_add=True, verbose_name='زمان ایجاد خبر ')),
                ('comment_count', models.CharField(max_length=50, verbose_name='تعداد نظر')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game', verbose_name='اخبار بازی')),
            ],
            options={
                'verbose_name': 'GameNews',
                'verbose_name_plural': 'GameNewss',
            },
        ),
        migrations.CreateModel(
            name='OperatingSystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_name', models.CharField(max_length=50, verbose_name='نام سیستم عامل')),
                ('description', models.TextField(verbose_name='توضیحات سیستم عامل')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games.game', verbose_name='بازی ها')),
            ],
            options={
                'verbose_name': 'سیستم عامل',
                'verbose_name_plural': 'سیستم عامل ها',
            },
        ),
    ]

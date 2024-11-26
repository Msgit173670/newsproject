# Generated by Django 4.0 on 2024-11-25 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('snsaccounts', '0002_alter_customuser_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='newsPhotoPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='タイトル')),
                ('comment', models.TextField(verbose_name='コメント')),
                ('image1', models.ImageField(upload_to='photos', verbose_name='イメージ1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='photos', verbose_name='イメージ2')),
                ('posted_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='newsphoto.category', verbose_name='カテゴリ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snsaccounts.customuser', verbose_name='ユーザー')),
            ],
        ),
    ]

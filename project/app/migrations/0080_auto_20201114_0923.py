# Generated by Django 3.1.2 on 2020-11-14 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0079_auto_20201113_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoDanDoQuanTrong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Độ quan trọng')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='Ngày tạo')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Cập nhật')),
                ('status', models.BooleanField(blank=True, default=True, null=True, verbose_name='Trạng thái')),
            ],
        ),
        migrations.CreateModel(
            name='HoDanLienLac',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Tình Trạng liên lạc')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='Ngày tạo')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Cập nhật')),
                ('status', models.BooleanField(blank=True, default=True, null=True, verbose_name='Sử dụng')),
            ],
        ),
        migrations.CreateModel(
            name='HoDanNhuCau',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default='', verbose_name='Nhu cầu')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='Ngày tạo')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='Cập nhật')),
                ('status', models.BooleanField(blank=True, default=True, null=True, verbose_name='Sử dụng')),
            ],
        )
    ]
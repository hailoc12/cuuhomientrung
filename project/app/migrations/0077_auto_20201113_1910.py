# Generated by Django 3.1.2 on 2020-11-13 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0076_merge_20201110_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalhodan',
            name='hodan_nhucau',
            field=models.SmallIntegerField(choices=[(0, 'Cần di chuyển tới nơi an toàn'), (1, 'Cần thức ăn, nước uống'), (2, 'Cần thuốc men')], default=0, null=True, verbose_name='Nhu cầu'),
        ),
        migrations.AddField(
            model_name='historicalhodan',
            name='hodan_nhucau_khac',
            field=models.TextField(blank=True, default='', verbose_name='Các nhu cầu khác'),
        ),
        migrations.AddField(
            model_name='hodan',
            name='hodan_nhucau',
            field=models.SmallIntegerField(choices=[(0, 'Cần di chuyển tới nơi an toàn'), (1, 'Cần thức ăn, nước uống'), (2, 'Cần thuốc men')], default=0, null=True, verbose_name='Nhu cầu'),
        ),
        migrations.AddField(
            model_name='hodan',
            name='hodan_nhucau_khac',
            field=models.TextField(blank=True, default='', verbose_name='Các nhu cầu khác'),
        ),
        migrations.AlterField(
            model_name='historicalhodan',
            name='do_quan_trong',
            field=models.SmallIntegerField(choices=[(0, 'Cực kỳ quan trọng'), (1, 'Rất quan trọng'), (2, 'Quan trọng'), (3, 'Ít quan trọng')], default=0, null=True, verbose_name='Độ quan trọng'),
        ),
        migrations.AlterField(
            model_name='historicalhodan',
            name='location',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='historicalhodan',
            name='trang_thai_lien_lac',
            field=models.SmallIntegerField(choices=[(0, 'Không rõ'), (1, 'Liên lạc được'), (2, 'Không liên lạc được')], default=0, null=True, verbose_name='Tình trạng liên lạc'),
        ),
        migrations.AlterField(
            model_name='hodan',
            name='do_quan_trong',
            field=models.SmallIntegerField(choices=[(0, 'Cực kỳ quan trọng'), (1, 'Rất quan trọng'), (2, 'Quan trọng'), (3, 'Ít quan trọng')], default=0, null=True, verbose_name='Độ quan trọng'),
        ),
        migrations.AlterField(
            model_name='hodan',
            name='location',
            field=models.CharField(blank=True, default='', max_length=200, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='hodan',
            name='trang_thai_lien_lac',
            field=models.SmallIntegerField(choices=[(0, 'Không rõ'), (1, 'Liên lạc được'), (2, 'Không liên lạc được')], default=0, null=True, verbose_name='Tình trạng liên lạc'),
        ),
        migrations.AlterField(
            model_name='trangthaihodan',
            name='status',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='Trạng thái'),
        ),
    ]
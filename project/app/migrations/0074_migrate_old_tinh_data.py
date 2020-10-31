# Generated by Django 3.1.2 on 2020-10-24 16:37

from django.db import migrations
import csv
from app.models import NewTinh, NewHuyen, NewXa, HoDan, CuuHo
from django.db import models

def migrate_tinh_id(apps, schema_editor):
    province_dict = {}
    with open('project/app/data/map_province.csv') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            if row[1] != "null":
                province_dict[int(row[0])] = int(row[1])
            else:
                province_dict[int(row[0])] = None
    for hodan in HoDan.objects.all():
        if hodan.tinh_id is not None:
            hodan.tinh_id = province_dict[hodan.tinh_id]
            hodan.save()
    for cuuho in CuuHo.objects.all():
        if cuuho.tinh_id is not None:
            cuuho.tinh_id = province_dict[cuuho.tinh_id]
            cuuho.save()
    
class Migration(migrations.Migration):

    dependencies = [
        ('app', '0073_import_location_data'),
    ]

    operations = [
        # Remove foreign key before update
        migrations.AlterField(
            model_name='hodan',
            name='tinh_id',
            field=models.IntegerField(db_index=True, null=True)
        ),
        migrations.AlterField(
            model_name='cuuho',
            name='tinh_id',
            field=models.IntegerField(db_index=True, null=True),
        ),
        migrations.RunPython(migrate_tinh_id),
        
    ]
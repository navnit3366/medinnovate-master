# Generated by Django 3.1.1 on 2020-10-13 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20201013_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='reference_file_1',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='reference_file_2',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='reference_file_3',
            field=models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d'),
        ),
    ]

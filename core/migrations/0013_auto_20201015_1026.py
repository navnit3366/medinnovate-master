# Generated by Django 3.1.1 on 2020-10-15 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20201013_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='prescriptions',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]

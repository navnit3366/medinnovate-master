# Generated by Django 3.1.1 on 2020-10-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='past_data',
            field=models.FileField(blank=True, upload_to='files/%Y/%m/%d'),
        ),
    ]

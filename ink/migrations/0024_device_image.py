# Generated by Django 4.1 on 2022-09-25 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0023_rename_device_url_device_ip_device_serial_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/devices', verbose_name='Изображение'),
        ),
    ]

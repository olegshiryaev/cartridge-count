# Generated by Django 4.1 on 2022-09-26 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0035_device_cartridge_device_image_device_ip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='image',
            field=models.ImageField(blank=True, default='img/devices/default_device.png', null=True, upload_to='img/devices', verbose_name='Изображение'),
        ),
    ]
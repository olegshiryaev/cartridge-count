# Generated by Django 4.1 on 2022-09-25 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0025_alter_device_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='image',
            field=models.ImageField(blank=True, default='default_device.png', null=True, upload_to='img/devices', verbose_name='Изображение'),
        ),
    ]

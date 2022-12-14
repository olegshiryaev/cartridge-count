# Generated by Django 4.1 on 2022-09-26 06:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0032_remove_device_cartridge_remove_device_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='unit_id',
            field=models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(limit_value=1, message='Минимум 1 символ'), django.core.validators.MaxLengthValidator(limit_value=4, message='Максимум 4 символа')], verbose_name='Код УЕ'),
        ),
    ]

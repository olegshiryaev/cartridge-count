# Generated by Django 4.1 on 2022-09-26 09:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0044_alter_device_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='amount',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(limit_value=0, message='Остаток не может быть меньше нуля')], verbose_name='Остаток'),
        ),
    ]
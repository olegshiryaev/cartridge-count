# Generated by Django 4.1 on 2022-08-11 08:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0002_alter_cartridge_options_alter_device_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='amount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Остаток'),
        ),
        migrations.AlterField(
            model_name='mount',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Кол-во'),
        ),
    ]
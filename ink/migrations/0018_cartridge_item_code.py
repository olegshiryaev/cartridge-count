# Generated by Django 4.1 on 2022-09-12 09:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0017_alter_cartridge_amount_alter_device_unit_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartridge',
            name='item_code',
            field=models.CharField(max_length=13, null=True, validators=[django.core.validators.MinLengthValidator(13)], verbose_name='Номенкл. код'),
        ),
    ]

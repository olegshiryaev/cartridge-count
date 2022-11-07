# Generated by Django 4.1 on 2022-09-26 10:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0049_alter_cartridge_storage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='item_code',
            field=models.CharField(max_length=15, null=True, validators=[django.core.validators.MinLengthValidator(13)], verbose_name='Номенкл. код'),
        ),
    ]
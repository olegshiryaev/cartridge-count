# Generated by Django 4.1 on 2022-08-11 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0007_alter_device_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cartridge',
            options={'ordering': ('model',), 'verbose_name': 'картридж', 'verbose_name_plural': 'Картриджи'},
        ),
    ]
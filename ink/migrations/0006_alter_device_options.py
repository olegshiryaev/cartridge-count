# Generated by Django 4.1 on 2022-08-11 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0005_alter_cartridge_amount_alter_mount_quantity'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='device',
            options={'ordering': ('-unit_id',), 'verbose_name': 'устройство', 'verbose_name_plural': 'Устройства'},
        ),
    ]

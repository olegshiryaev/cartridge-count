# Generated by Django 4.1 on 2022-09-26 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0045_alter_cartridge_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartridge',
            name='storage',
        ),
    ]

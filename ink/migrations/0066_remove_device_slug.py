# Generated by Django 4.1 on 2022-11-07 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0065_mount_storage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='slug',
        ),
    ]

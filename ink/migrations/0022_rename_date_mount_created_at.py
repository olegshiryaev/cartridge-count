# Generated by Django 4.1 on 2022-09-25 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0021_alter_device_device_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mount',
            old_name='date',
            new_name='created_at',
        ),
    ]

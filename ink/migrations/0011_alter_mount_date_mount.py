# Generated by Django 4.1 on 2022-08-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0010_alter_mount_quantity_alter_mount_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mount',
            name='date_mount',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата установки'),
        ),
    ]

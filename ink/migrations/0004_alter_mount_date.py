# Generated by Django 4.1 on 2022-08-11 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0003_alter_cartridge_amount_alter_mount_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mount',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]

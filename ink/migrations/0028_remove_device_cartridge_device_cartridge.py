# Generated by Django 4.1 on 2022-09-25 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0027_device_cartridge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='cartridge',
        ),
        migrations.AddField(
            model_name='device',
            name='cartridge',
            field=models.ManyToManyField(null=True, to='ink.cartridge', verbose_name='Картридж'),
        ),
    ]

# Generated by Django 4.1 on 2022-09-26 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0048_alter_cartridge_item_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartridge',
            name='storage',
            field=models.ManyToManyField(default='Архангельск', to='ink.storage', verbose_name='Склад'),
        ),
    ]
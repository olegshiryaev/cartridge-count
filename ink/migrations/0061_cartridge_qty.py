# Generated by Django 4.1 on 2022-10-31 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0060_storage_purchase_alter_storage_cartridge_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartridge',
            name='qty',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Количество на складах'),
        ),
    ]

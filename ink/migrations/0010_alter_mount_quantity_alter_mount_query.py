# Generated by Django 4.1 on 2022-08-11 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0009_remove_mount_date_mount_date_mount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mount',
            name='quantity',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='mount',
            name='query',
            field=models.CharField(max_length=40, verbose_name='Заявка'),
        ),
    ]

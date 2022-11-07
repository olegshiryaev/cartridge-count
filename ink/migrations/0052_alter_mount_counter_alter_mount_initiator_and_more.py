# Generated by Django 4.1 on 2022-09-26 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0051_mount_counter_mount_initiator_mount_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mount',
            name='counter',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Счётчик'),
        ),
        migrations.AlterField(
            model_name='mount',
            name='initiator',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Инициатор'),
        ),
        migrations.AlterField(
            model_name='mount',
            name='note',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Примечание'),
        ),
    ]

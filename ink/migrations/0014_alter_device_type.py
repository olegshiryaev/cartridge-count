# Generated by Django 4.1 on 2022-08-18 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ink', '0013_alter_mount_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='type',
            field=models.CharField(choices=[('МФУ', 'МФУ'), ('Принтер лазерный', 'Принтер лазерный'), ('Принтер струйный', 'Принтер струйный'), ('Принтер матричный', 'Принтер матричный'), ('Принтер сублимационный', 'Принтер сублимационный'), ('Принтер термо-трансферный', 'Принтер термо-трансферный')], max_length=50, verbose_name='Тип устройства'),
        ),
    ]

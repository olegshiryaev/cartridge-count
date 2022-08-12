from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from datetime import date
from django.utils.text import slugify


# Create your models here.

class Device(models.Model):  # Модель "Устройство"
    TYPE_CHOICES = [
        ('МФУ', 'МФУ'),
        ('Принтер лазерный', 'Принтер лазерный'),
        ('Принтер струйный', 'Принтер струйный'),
    ]

    unit_id = models.CharField(max_length=10, validators=[MinLengthValidator(1), MaxLengthValidator(4)],
                               verbose_name="Код УЕ")
    type = models.CharField(
        max_length=50, choices=TYPE_CHOICES, verbose_name="Тип устройства")
    model = models.CharField(max_length=100, verbose_name="Модель")
    location = models.CharField(max_length=200, verbose_name="Расположение")

    class Meta:
        verbose_name = 'устройство'
        verbose_name_plural = 'Устройства'
        ordering = ('unit_id',)


    def __str__(self):
        return f'{self.unit_id} - {self.model}'


class Storage(models.Model):  # Модель "Склад"
    name = models.CharField(max_length=50, verbose_name="Склад")

    class Meta:
        verbose_name = 'склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return f'{self.name}'


class Cartridge(models.Model):  # Модель "Картридж"
    model = models.CharField(max_length=100, verbose_name="Наименование")
    amount = models.PositiveIntegerField(
        validators=[MinValueValidator(0)], default=0, verbose_name="Остаток")
    storage = models.ManyToManyField(Storage)

    class Meta:
        verbose_name = 'картридж'
        verbose_name_plural = 'Картриджи'
        ordering = ('model',)

    def __str__(self):
        return f'{self.model}'

    def has_amount(self):
        return self.amount > 0


class Mount(models.Model):  # Модель "Установки картриджа на устройство"
    date = models.DateField(
        default=date.today, verbose_name="Дата установки")
    cartridge = models.ForeignKey(
        Cartridge, null=True, on_delete=models.SET_NULL, verbose_name="Картридж")
    device = models.ForeignKey(
        Device, null=True, on_delete=models.SET_NULL, verbose_name="Устройство")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кол-во")
    query = models.CharField(max_length=50, verbose_name="Заявка")

    class Meta:
        verbose_name = 'установку картриджа'
        verbose_name_plural = 'Установки картриджей'

    def __str__(self):
        return f'{self.date} | {self.cartridge} | {self.device} | {self.quantity} | {self.query}'

    def remaining_stocky(self):
        return self.cartridge.amount - self.quantity
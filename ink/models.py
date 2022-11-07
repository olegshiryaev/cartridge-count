from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from datetime import date
from django.utils.text import slugify
from django.contrib.auth.models import User


# Create your models here.
class Storage(models.Model):  # Модель "Склад"

    STORAGE_CHOICES = (
        ('Архангельск', 'Архангельск'),
        ('Нарьян-Мар', 'Нарьян-Мар'),
    )

    name = models.CharField(max_length=15, choices=STORAGE_CHOICES, verbose_name="Склад")

    class Meta:
        verbose_name = 'склад'
        verbose_name_plural = 'Склады'

    def __str__(self):
        return f'{self.name}'

class Cartridge(models.Model):  # Модель "Картридж"

    COLOR_CHOICES = (
            ('C', 'Cyan'),
            ('M', 'Magenta'),
            ('Y', 'Yellow'),
            ('K', 'Black'),
    )

    item_code = models.CharField(max_length=15, validators=[
        MinLengthValidator(13)], null=True,
        verbose_name="Номенкл. код")
    model = models.CharField(max_length=100, verbose_name="Наименование")
    color = models.CharField(max_length=1, choices=COLOR_CHOICES, default='K', verbose_name='Цвет')
    amount = models.PositiveIntegerField(validators=[
        MinValueValidator(
            limit_value=0, 
            message='Остаток не может быть меньше нуля'
        ) 
            ], default=0, verbose_name="Остаток")
    storage = models.ManyToManyField(Storage, default = 'Архангельск',  verbose_name="Склад")

    class Meta:
        verbose_name = 'картридж'
        verbose_name_plural = 'Картриджи'
        ordering = ('model',)

    def __str__(self):
        return f'{self.item_code} - {self.model}'


class CartridgePurchase(models.Model):
    cartridge_id = models.ForeignKey(Cartridge, on_delete=models.CASCADE,null=True, related_name='Cartridgepurchase')
    date_posted = models.DateField(default=date.today)
    purchase_date = models.DateField(default=date.today)
    invoice_number = models.PositiveIntegerField(null=True, blank=True, verbose_name='Накладная')
    qty_ordered = models.PositiveIntegerField(null=True, blank=True , verbose_name= 'Количество')
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    note = models.TextField(null=True, blank=True, verbose_name='Примечание')

    class Meta:
        ordering = ['-purchase_date']
    def __str__(self):
        return str(self.cartridge)

class Device(models.Model):  # Модель "Устройство"
    TYPE_CHOICES = [
        ('МФУ', 'МФУ'),
        ('Принтер лазерный', 'Принтер лазерный'),
        ('Принтер струйный', 'Принтер струйный'),
        ('Принтер матричный', 'Принтер матричный'),
        ('Принтер сублимационный', 'Принтер сублимационный'),
        ('Принтер термо-трансферный', 'Принтер термо-трансферный'),
    ]

    unit_id = models.CharField(max_length=8, validators=[
        MinLengthValidator(
            limit_value=1,
            message='Минимум 1 символ'
        ),
        MaxLengthValidator(
            limit_value=4,
            message='Максимум 4 символа'
        )], verbose_name="Код УЕ")
    type = models.CharField(
        max_length=50, choices=TYPE_CHOICES, verbose_name="Тип устройства")
    model = models.CharField(max_length=100, verbose_name="Модель")
    location = models.CharField(max_length=200, verbose_name="Расположение")
    image = models.ImageField(upload_to='img/devices', null=True, blank=True, verbose_name="Изображение")
    cartridge = models.ManyToManyField(Cartridge, verbose_name="Совместимые картриджи")
    color = models.BooleanField(default=False, verbose_name='Цветной')
    ip = models.URLField(null=True, blank=True, verbose_name="IP-адрес")
    serial_number = models.CharField(max_length=50, null=True, blank=True, verbose_name="Серийный номер")

    class Meta:
        verbose_name = 'устройство'
        verbose_name_plural = 'Устройства'
        ordering = ('unit_id',)


    def __str__(self):
        return f'{self.unit_id} - {self.model}'


class Mount(models.Model):  # Модель "Установки картриджа на устройство"
    created_at = models.DateField(
        default=date.today, verbose_name="Дата установки")
    storage = models.ForeignKey(Storage, null=True, on_delete=models.PROTECT, verbose_name="Склад")
    cartridge = models.ForeignKey(
        Cartridge, null=True, on_delete=models.SET_NULL, verbose_name="Картридж")
    device = models.ForeignKey(
        Device, null=True, on_delete=models.SET_NULL, verbose_name="Устройство")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кол-во")
    query = models.CharField(max_length=50, verbose_name="Заявка")
    initiator = models.CharField(max_length=100, null=True, verbose_name="Инициатор")
    counter = models.PositiveIntegerField(null=True, blank=True, verbose_name="Счётчик")
    note = models.CharField(max_length=200, null=True, blank=True, verbose_name="Примечание")
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        verbose_name = 'установку картриджа'
        verbose_name_plural = 'Установки картриджей'

    def __str__(self):
        return f'{self.created_at} | {self.cartridge} | {self.device} | {self.quantity} | {self.query}'
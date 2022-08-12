from dataclasses import fields
import django_filters

from .models import *


class MountFilter(django_filters.FilterSet):  # Фильтр по полю "Заявка"

    class Meta:
        model = Mount
        fields = ['query', 'date']


# Фильтр по полю "Наименование" картриджа
class CartridgeFilter(django_filters.FilterSet):
    
    class Meta:
        model = Cartridge
        fields = ['model']



class DeviceFilter(django_filters.FilterSet):

    class Meta:
        model = Device
        fields = ['unit_id', 'type', 'model']

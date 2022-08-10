import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class MountFilter(django_filters.FilterSet):  # Фильтр по полю "Заявка"

    class Meta:
        model = Mount
        fields = ['query']


# Фильтр по полю "Наименование" картриджа
class CartridgeFilter(django_filters.FilterSet):

    class Meta:
        model = Cartridge
        fields = ['model']

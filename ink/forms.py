from django import forms
from django.forms import ModelForm, TextInput, Select
from .models import Device, Mount


class DeviceForm(forms.ModelForm):  # Форма для модели "Устройство"
    class Meta:
        model = Device
        fields = '__all__'
        exclude = ['slug']
        widgets = {
            'unit_id': TextInput(attrs={'class': 'col-md-12 form-control'}),
            'type': Select(attrs={'class': 'col-md-12 form-control'}),
            'model': TextInput(attrs={'class': 'col-md-12 form-control'}),
            'location': TextInput(attrs={'class': 'col-md-12 form-control'}),
        }


class DeviceUpdateForm(forms.ModelForm):  # Форма для редактирования устройства
    class Meta:
        model = Device
        fields = '__all__'
        exclude = ['unit_id', 'slug']
        widgets = {
            'type': Select(attrs={'class': 'col-md-12 form-control'}),
            'model': TextInput(attrs={'class': 'col-md-12 form-control'}),
            'location': TextInput(attrs={'class': 'col-md-12 form-control'}),
        }


class MountForm(ModelForm):  # Форма установки картриджа на устройство
    class Meta:
        model = Mount
        fields = '__all__'
        widgets = {
            'cartridge': Select(attrs={'class': 'col-md-12 form-control'}),
            'device': Select(attrs={'class': 'col-md-12 form-control'}),
            'quantity': TextInput(attrs={'class': 'col-md-12 form-control'}),
            'query': TextInput(attrs={'class': 'col-md-12 form-control'}),
        }

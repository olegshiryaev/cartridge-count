from django.contrib import admin
from .models import Device, Cartridge, Mount, Storage

# Register your models here.


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    # fields = ['unit_id', 'type', 'model', 'location']
    exclude = ['slug']
    # prepopulated_fields = {'slug': ('unit_id', 'model')}
    list_display = ['unit_id', 'type', 'model', 'location']
    list_editable = ['location']
    ordering = ['unit_id']
    list_per_page = 20
    search_fields = ['unit_id__startswith', 'model']
    list_filter = ['type']


@admin.register(Cartridge)
class CartridgeAdmin(admin.ModelAdmin):
    list_display = ['model', 'amount']
    list_editable = ['amount']
    list_per_page = 20
    search_fields = ['model']
    list_filter = ['storage']


@admin.register(Mount)
class MountAdmin(admin.ModelAdmin):
    list_display = ['cartridge', 'device', 'quantity', 'query']
    list_per_page = 20
    search_fields = ['cartridge', 'device', 'query']


@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

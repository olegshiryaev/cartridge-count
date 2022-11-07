from django.contrib import admin
from .models import Device, Cartridge, Mount, Storage

# Register your models here.

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    # fields = ['unit_id', 'type', 'model', 'location']
    # exclude = ['slug']
    # prepopulated_fields = {'slug': ('unit_id', 'model')}
    list_display = ['unit_id', 'type', 'model', 'location']
    list_editable = ['type', 'model', 'location']
    ordering = ['unit_id']
    list_per_page = 20
    search_fields = ['unit_id__startswith', 'model']
    list_filter = ['type']

@admin.register(Cartridge)
class CartridgeAdmin(admin.ModelAdmin):
    list_display = ['item_code', 'model', 'color', 'amount']
    list_editable = ['color', 'amount']
    list_per_page = 20
    search_fields = ['item_code', 'model', 'color']
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
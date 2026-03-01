from django.contrib import admin

from netmanager.models import Customer, Asset, AssetType


@admin.register(Customer)
class CostumerAdmin(admin.ModelAdmin):
    list_display = ['name', 'document', 'contact']

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'address', 'type', 'status', 'costumer']

@admin.register(AssetType)
class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

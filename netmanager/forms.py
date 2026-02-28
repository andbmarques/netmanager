from django import forms
from .models import Asset, Customer, AssetType


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'document', 'contact']


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['hostname', 'address', 'type', 'costumer']

class AssetTypeForm(forms.ModelForm):
    class Meta:
        model = AssetType
        fields = ['name']
from django import forms
from .models import Asset, Customer, AssetType


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'document', 'contact']


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['hostname', 'address', 'type', 'customer']
        widgets = {
            'asset_type': forms.Select(attrs={
                'class': 'bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 cursor-pointer',
            }),
        }

class AssetTypeForm(forms.ModelForm):
    class Meta:
        model = AssetType
        fields = ['name']
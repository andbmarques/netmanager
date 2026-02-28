from django.db import models
from django.conf import settings

class AssetType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class AssetStatus(models.Model):
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    latency = models.FloatField(null=True)

class Customer(models.Model):
    name = models.CharField(max_length=200, null=False)
    document = models.CharField(max_length=14, null=False, unique=True)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Asset(models.Model):
    hostname = models.CharField(max_length=200, null=True, unique=True)
    address = models.GenericIPAddressField()
    type = models.ForeignKey(AssetType, on_delete=models.PROTECT)
    status = models.ForeignKey(AssetStatus, on_delete=models.PROTECT, null=True)
    costumer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT
    )
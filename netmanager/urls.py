"""
URL configuration for netmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name

from django.contrib import admin
from django.urls import path, include
from .views import HomeView, CustomerCreateView, CustomerListView, AssetListView, AssetCreateView, AssetTypeCreateView, \
    AssetTypeListView, CustomerDetailView, CustomerDeleteView, CustomerUpdateView, AssetTypeDeleteView, \
    AssetTypeUpdateView, AssetDeleteView, AssetDetailView, AssetUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('', HomeView.as_view()),
    path('customers/', CustomerListView.as_view()),
    path('customers/new/', CustomerCreateView.as_view()),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name="customer-detail"),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view()),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view()),
    path('assets/', AssetListView.as_view()),
    path('assets/new/', AssetCreateView.as_view()),
    path('assets/<int:pk>/delete/', AssetDeleteView.as_view()),
    path('assets/<int:pk>/edit/', AssetUpdateView.as_view()),
    path('assets/<int:pk>/', AssetDetailView.as_view(), name="asset-detail"),
    path('asset_type/', AssetTypeListView.as_view()),
    path('asset_type/new/', AssetTypeCreateView.as_view()),
    path('asset_type/<int:pk>/delete/', AssetTypeDeleteView.as_view()),
    path('asset_type/<int:pk>/edit/', AssetTypeUpdateView.as_view()),
]

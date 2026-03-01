from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, DeleteView, UpdateView
from .models import Customer, Asset, AssetType
from .forms import CustomerForm, AssetForm, AssetTypeForm

# CUSTOMERS
class CustomerListView(ListView):
    model = Customer
    template_name = "netmanager/customers/customer_list.html"
    paginate_by = 10

class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "netmanager/customers/customer_create.html"
    success_url = "/customers/"

class CustomerDetailView(DetailView):
    model = Customer
    template_name = "netmanager/customers/customer_details.html"
    context_object_name = "customer"

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = "netmanager/customers/customer_delete.html"
    success_url = "/customers/"

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)

            context['error_message'] = "It's not possible to delete the Customer because there are Assets linked to it."

            return self.render_to_response(context)

class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "netmanager/customers/customer_create.html"

    def get_success_url(self):
        return reverse_lazy("customer-detail", kwargs={"pk": self.object.pk})

# ASSETS

class AssetListView(ListView):
    model = Asset
    template_name = "netmanager/assets/asset_list.html"
    paginate_by = 10

class AssetCreateView(CreateView):
    model = Asset
    form_class = AssetForm
    template_name = 'netmanager/assets/asset_create.html'
    success_url = '/assets/'

class AssetDeleteView(DeleteView):
    model = Asset
    template_name = "netmanager/assets/asset_delete.html"
    success_url = "/assets/"

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)

            context['error_message'] = "It's not possible to delete the Asset because there are objects linked to it."

            return self.render_to_response(context)

class AssetDetailView(DetailView):
    model = Asset
    template_name = "netmanager/assets/asset_details.html"
    context_object_name = "asset"

class AssetUpdateView(UpdateView):
    model = Asset
    form_class = AssetForm
    template_name = "netmanager/assets/asset_create.html"

    def get_success_url(self):
        return reverse_lazy("asset-detail", kwargs={"pk": self.object.pk})

# ASSETS TYPES

class AssetTypeListView(ListView):
    model = AssetType
    template_name = 'netmanager/asset_type/asset_type_list.html'
    paginate_by = 10

class AssetTypeCreateView(CreateView):
    model = AssetType
    form_class = AssetTypeForm
    template_name = 'netmanager/asset_type/asset_type_create.html'
    success_url = '/asset_type/'

class AssetTypeDeleteView(DeleteView):
    model = AssetType
    template_name = "netmanager/asset_type/asset_type_delete.html"
    success_url = "/asset_type/"
    context_object_name = "asset_type"

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)

            context['error_message'] = "It's not possible to delete the Asset Type because there are Assets linked to it."

            return self.render_to_response(context)

class AssetTypeUpdateView(UpdateView):
    model = AssetType
    form_class = AssetTypeForm
    template_name = "netmanager/asset_type/asset_type_create.html"
    success_url = "/asset_type/"

# OTHERS

class HomeView(ListView):
    template_name = "netmanager/home.html"
    model = Asset
    context_object_name = "assets"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['customers'] = Customer.objects.all()

        return context
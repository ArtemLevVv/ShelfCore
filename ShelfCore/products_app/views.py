from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView
from django.shortcuts import render

from django.http import JsonResponse
from django.views import View

from products_app.models import Product, Category
from products_app.forms import ProductForm
# Create your views here.
class ProductShowView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView,
    ):

    model = Product
    paginate_by = 1
    context_object_name = 'products'
    template_name = 'products/products.html'
    permission_required= 'products_app.view_product'

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context["nav"] = True
        return context
    
class ProductInfoView(View):
    def get(self, request, pk):
        
        product = Product.objects.get(pk=pk)
        
        data = {
            "name": product.name,
            "barcode": product.barcode,
            "category": product.category.name,
            "category_id": product.category.id,
            "unit": product.unit,
            "age_restricted": product.age_restricted,
            "is_active": product.is_active,
        }
        
        return JsonResponse(data)
    
class ProductEditView(UpdateView):
    model = Product
    form_class = ProductForm
    
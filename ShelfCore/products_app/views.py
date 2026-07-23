from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, UpdateView, CreateView
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from django.http import JsonResponse, request
from django.views import View

from products_app.models import Product, Category
from products_app.forms import ProductForm, CategoryForm

import json
# Create your views here.
class ProductShowView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ListView,
    ):

    model = Product
    paginate_by = 10
    context_object_name = 'products'
    template_name = 'products/products.html'
    permission_required= 'products_app.view_product'

    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context["nav"] = True
        return context
    
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        
        search = request.GET.get('name-search')
        category = request.GET.get('category')
        is_active = request.GET.get('is-active')
        age_restricted = request.GET.get('age-restricted')
        print(f'search:{search};')
        print(f'category:{category};')
        print(f'is active:{is_active};')
        print(f'is age restricted:{age_restricted};')
        
        if search:
            products = products.filter(
                name__icontains=search
            )
        if category:
            products = products.filter(
                category_id=category
            )
        if is_active:
            if is_active == "True":
                is_active = True
            else:
                is_active = False
            products = products.filter(
                is_active=is_active
            )
        if age_restricted:
            if age_restricted == 'True':
                age_restricted = True
            else:
                age_restricted = False
            products = products.filter(
                age_restricted= age_restricted
            )
        
        paginator = Paginator(products,10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context = {
            "products": page_obj,
            "page_obj": page_obj,
            "categories": Category.objects.all(),
            "nav": True,
            'search': search,
            'category': category,
            'is-active':is_active,
            'age-restricted': age_restricted
        }
        return render(request, "products/products.html", context)
class ProductInfoView(
    View,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ):
    
    permission_required= 'products_app.view_product'
    
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
    
class ProductEditView(
    UpdateView,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ):
    
    permission_required= 'products_app.change_product'
    
    def post(self, request, pk):
        product = get_object_or_404(
            Product,
            pk= pk
        )
        
        if not request.user.has_perm(
            'products_app.change_product'
        ):
            return JsonResponse(
                {"success":False},
                status= 403,
            )
        
        data = json.loads(
            request.body
        )
        
        product.name = data["name"]
        product.barcode = data["barcode"]
        product.category_id = data["category"]
        product.unit = data["unit"]
        
        product.age_restricted = data["age_restricted"]
        product.is_active = data['is_active']
        
        product.save()
        
        return JsonResponse({
            "success": True,
            "product":{
                "id": product.id,
                "name": product.name,
                "barcode": product.barcode,
                "category_id": product.category.id,
            }
        })
        
class ProductCreateView(
    CreateView,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ):
    
    model = Product
    form_class = ProductForm
    success_url = "/products/show/"
    template_name = 'products/product_create.html'
    permission_required = 'products_app.add_product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nav'] = True 
        return context
    
class ProductCategoryView(
    ListView,
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ):
    
    model = Category
    paginate_by = 10
    context_object_name = 'categories'
    template_name = 'category/category.html'
    permission_required= 'products_app.view_category'
    
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["nav"] = True
        return context

class ProductCategoryCreate(
    CreateView,
    LoginRequiredMixin,
    PermissionRequiredMixin
    ):
    
    model = Category
    form_class = CategoryForm
    success_url = "/products/category/"
    template_name = 'category/category_create.html'
    permission_required = 'products_app.add_category'
    
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["nav"] = True
        return context
    
from django.urls import path

from .views import ProductShowView, ProductInfoView, ProductEditView, ProductCreateView, ProductCategoryView, ProductCategoryCreate

urlpatterns = [
    path('show/', ProductShowView.as_view(), name= 'product_show'),
    path('<int:pk>/info/', ProductInfoView.as_view(), name= 'product_info'),
    path('<int:pk>/edit/', ProductEditView.as_view(), name= 'product_edit'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('category/', ProductCategoryView.as_view(), name='product_category'),
    path('category/create/', ProductCategoryCreate.as_view(), name='product_category_create'),
]

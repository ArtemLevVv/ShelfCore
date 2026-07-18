from django.urls import path

from .views import ProductShowView, ProductInfoView

urlpatterns = [
    path('show/', ProductShowView.as_view(), name= 'product_show'),
    path('<int:pk>/info/', ProductInfoView.as_view(), name= 'product_info')
]

from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class ProductView(TemplateView):
    template_name = 'products/products.html'
    
    def get_context_data(self, **kwargs) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context["nav"] = True
        return context
    
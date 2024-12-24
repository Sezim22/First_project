from django.contrib.messages import DEFAULT_TAGS
from django.urls import reverse_lazy

from .models import Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ProductForm

class ProductListViews(ListView):
    queryset = Product.objects.all()
    template_name = 'product_list.html'
    context_object_name = 'products'



class ProductDetailViews(DetailView):
    queryset = Product.objects.all()
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductCreateViews(CreateView):
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

class ProductUpdateViews(UpdateView):
    queryset =  Product.objects.all()
    template_name = 'product_update.html'
    form_class = ProductForm
    success_url = reverse_lazy('product_list')

class ProductDeleteViews(DeleteView):
        queryset = Product.objects.all()
        template_name = 'product_delete.html'
        success_url = reverse_lazy('product_list')

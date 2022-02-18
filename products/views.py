from django.forms.formsets import formset_factory
from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . models import Product
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . forms import ProductForm
from django.forms import inlineformset_factory

class ProductListView(generic.ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Product.objects.all()

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Product.objects.all()

class ProductCreateView(CreateView):
    model = Product
    fields = [
        'name',
        'unit_of_measurement',
        'active',
        'price',
        'is_bread',
        'control_stock',
        ]
    success_url = '/products/list/'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/product_update.html'
    fields = [
        'name',
        'unit_of_measurement',
        'active',
        'price',
        'is_bread',
        'control_stock',
        ]
    success_url = '/products/list/'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class ProductDeleteView(DeleteView):
    model = Product
    success_url = '/products/list/'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def priceUpdate(request):
    
    """
    ProductFormSet = inlineformset_factory(parent_model=None, model=Product,)
    #products = Product.objects.all()
    #form = ProductForm()
    #ProductFormSet = formset_factory(ProductForm)
    
    formset = ProductFormSet()
    context = {
        #'products':products,
        'formset': formset,
    }
    #print(products)
    return render(request, 'products/prices_update.html', context)
    """
    return render(request, 'products/prices_update.html')
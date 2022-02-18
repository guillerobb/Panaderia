from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . models import Customer, Contact
from . forms import ContactForm

@login_required(login_url='/login/')
def index(request):
    print(request.user.is_authenticated)
    print(request.method)
    print(request.user)
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                #return redirect('index')
                return render(request, 'index.html')
            else:
                messages.info(request, 'Usuario o Contraseña es incorrecta')
        
    context = {}
    return render(request, 'accounts/login.html', context)
    

class CustomerListView(generic.ListView):
    template_name = 'customer/customer_list.html'
    context_object_name = 'customer_list'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Customer.objects.all()

class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name  = 'customers/customer_detail.html'
    context_object_name = 'customer_detail'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        return Customer.objects.all()

class CustomerCreateView(CreateView):
    model = Customer
    fields = [
        'business_name',
        'active',
        'profile_picture'
    ]
    success_url = '/customers/'
    
    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customers/customer_update.html'
    fields = [
        'business_name',
        'active',
        'profile_picture'
    ]
    success_url = '/customers/'
    success_message = 'Cliente Guardado'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = '/customers/'

@login_required(login_url='loginPage')
def CustomerContactList(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    contacts_queryset = customer.get_contacts()
    context = {
        'customer':customer,
        'contacts':contacts_queryset,
    }
    print(contacts_queryset)
    return render(request, 'customers/contact_list.html', context)

@login_required(login_url='/login/')
class ContactDetailView(generic.DetailView):
    model = Contact
    template_name = 'customers/contact_detail.html'

    context_object_name = 'contact_detail'

    def get_queryset(self):
        return Customer.objects.all()

@login_required(login_url='/login/')
def ContactCreateView(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)

    form = ContactForm(initial={'customer':customer})
    
    context = {
        'customer':customer,
        'form':form,
    }

    return render(request, 'customers/contact_form.html',context)

@login_required(login_url='/login/')
def AddContact(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    if  request.method == 'POST':
        
        form = ContactForm(request.POST)
    
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    
    context = {
       'customer':customer,
    }
    return render(request, 'customers/contact_list.html', context)

@login_required(login_url='/login/')
def ContactUpdateView(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        
        if form.is_valid():
            form.save()
            context ={
                'customer':contact.customer,
            }
        return render(request, 'customers/contact_list.html', context)
    else:
        context = {
            'contact':contact,
            'form':form,
        }
        return render(request, 'customers/contact_update.html', context)

class ContactDeleteView(DeleteView):
    model = Contact
    success_url = '/customers-contact/{customer_id}'

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
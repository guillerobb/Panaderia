from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import Sale, Detail
from customers.models import Contact, Customer
from django.http import JsonResponse

# Create your views here.
def createSale(request):
    print('createSale')

    SaleFormSet = inlineformset_factory(Sale, Detail, fields=('product', 'amount', 'price'))
    #customer = Customer.objects.get(id=pk)
    #contact = Contact.objects.filter(customer = pk).first()
    #contact = contact_queryset.first()
    #sale = Sale(customer=customer, contact = contact)
    
    
    #formSet = SaleFormSet(instance=sale)
    formSet = SaleFormSet()

    if request.method == 'POST':
        print(request)
        #formSet = SaleFormSet(request.POST, instance=sale)
        #sale.save()
        if formSet.is_valid():
            formSet.save()
            return redirect('/') 
      
    customers = Customer.objects.all()
    context = {
        'customers': customers,
        'formSet':formSet,
       # 'customer':customer,
    }
    return render(request, 'sales/sale_form.html', context)
    

def saleUpdate(request, pk):
    sale = Sale.objects.get(id=pk)
    context = {
        'sale':sale,
    }
    return render(request, 'sales/sale_update.html', context)

def salesList(request):
    """
    customer_list = Customer.objects.all()
    context = {
        'customer_list':customer_list,
    }"""


    sales = Sale.objects.all()
    context = {
        'sales': sales
    }
    return render(request, 'sales/sale_list.html', context)

def getContactsAjax(request):
    print('getContactsAjax')
    print(request)
    if request.method == "POST":
        customer_id = request.POST['customer_id']
        try:
            customer = Customer.objects.filter(id = customer_id).first()
            contacts = Contact.objects.filter(customer = customer)
        except Exception:
            pass
            #data['error_message'] = 'error'
            #return JsonResponse(data)
        return JsonResponse(list(contacts.values('id', 'first_name')), safe = False)

def  getSaleAjax(request):
    print('getSaleAjax')
    print('Request: ' + request)
    if request.method == 'POST':
        SaleFormSet = inlineformset_factory(Sale, Detail, fields=('product', 'amount', 'price'))
        customer_id = request.POST['customer_id']
        contact_id = request.POST['contact_id']
        customer = Customer.objects.get(id=customer_id)
        contact = Contact.objects.get(id = contact_id)
        #contact = contact_queryset.first()
        sale = Sale(customer=customer, contact = contact)


        #formSet = SaleFormSet(instance=sale)
        formSet = SaleFormSet()

        context = {
            'formSet':formSet,
            # 'customer':customer,
        }

    #return JsonResponse(context, safe=False)
    return render(request, 'sales/sale_form_table_products.html', context)

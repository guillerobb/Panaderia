from django.forms import ModelForm
from .models import Sale
from customers.models import Customer

CUSTOMER_CHOICES = Customer.objects.all()

class SaleForm(ModelForm):

    class Meta:
        model = Sale
         
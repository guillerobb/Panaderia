from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from customers.models import Customer, Contact
from products.models import Product
from django.db.models import Avg, Count, Min, Sum
from django.contrib.auth.models import User

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE),
    date = models.DateTimeField('Fecha', default=timezone.now, editable=True)
    created = models.DateTimeField('Creado', default=timezone.now, editable=False)
    updated = models.DateTimeField('Actualizado', auto_now=True, editable=False)

    def get_total(self):
        return Detail.objects.filter(sale__pk = self.pk).aggregate(Sum('price'))

    def get_author_name(self):
        user = User.objects.get(id=self.pk)
        print(user.get_full_name)
        #saleman = User.objects.filter(pk = author)
        
        return user.username

class Detail(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField('Cantidad', default=0)
    price = models.DecimalField('Precio',max_digits=18, decimal_places=2,blank=True,null=True)
from django.db import models

class Customer(models.Model):
    business_name = models.CharField("Nombre", max_length=40)
    active = models.BooleanField("Estado", default=True)
    profile_picture = models.ImageField("Imágen/Logo", blank=True, null=True)

    def __str__(self):
        return self.business_name

    def get_contacts(self):
        return Contact.objects.filter(customer__pk=self.pk)

class Contact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    active = models.BooleanField(default=True)
    profile_picture = models.ImageField(blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
from django.db import models
from django.utils import timezone

class Product(models.Model):
    class UnitOfMeasurement(models.TextChoices):
        KILOGRAM = 'KG', ('Kilogramo')
        UNIT = 'U', ('Unidades')

    name = models.CharField('Nombre',max_length=40,blank=True,null=True)
    unit_of_measurement = models.CharField('Unidad de medida', max_length=4, choices=UnitOfMeasurement.choices, default=UnitOfMeasurement.UNIT)
    active = models.BooleanField('Estado', default=False)
    price = models.DecimalField('Precio',max_digits=18, decimal_places=2,blank=True,null=True)
    is_bread = models.BooleanField('Es Pan',default=False)
    control_stock = models.BooleanField('Controla Stock',default=False)
    created = models.DateTimeField('Creado', default=timezone.now, editable=False)
    updated = models.DateTimeField('Actualizado', auto_now=True, editable=False)

    def __str__(self) :
        return self.name
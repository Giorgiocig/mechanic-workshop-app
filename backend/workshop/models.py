from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    """
    It manage clients personal data 
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    registration_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Vehicule(models.Model):
    """
    It manage vehicules linked to a Client
    """
    FUEL_TYPE_CHOICES = [
        ('B', 'Benzina'),
        ('D', 'Diesel'),
        ('G', 'GPL/Metano'),
        ('E', 'Elettrico'),
        ('H', 'Ibrido'),
    ]

    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='vehicules')
    number_plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField(blank=True, null=True)
    vin = models.CharField(max_length=17, unique=True, blank=True, null=True, verbose_name="Numero di Telaio (VIN)")
    fuel = models.CharField(max_length=1, choices=FUEL_TYPE_CHOICES, default='B')
    kilometrage = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.number_plate})"
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client, Vehicule

admin.site.register(Client)
admin.site.register(Vehicule)

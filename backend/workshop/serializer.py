from rest_framework import serializers
from .models import  Client, Vehicule

class VehiculeSerializer(serializers.ModelSerializer):
  class Meta:
    model=Vehicule
    fields='__all__'

class ClientSerializer(serializers.ModelSerializer):
  vehicules = VehiculeSerializer(many=True, read_only=True)

  class Meta:
    model=Client
    fields='__all__'
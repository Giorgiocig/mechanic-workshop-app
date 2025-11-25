from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from workshop.models import Client, Vehicule
from workshop.serializer import ClientSerializer, VehiculeSerializer

# Client Views
class ClientViewSet(viewsets.ModelViewSet):
    """
    Gestione completa dei clienti:
    - GET /clients/ → lista
    - POST /clients/ → crea
    - GET /clients/<id>/ → dettaglio
    - PUT /clients/<id>/ → aggiorna
    - DELETE /clients/<id>/ → elimina
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


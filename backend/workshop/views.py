from rest_framework import status, viewsets
from workshop.models import Client, Vehicule
from workshop.serializer import ClientSerializer, VehiculeSerializer

# Client Views
class ClientViewSet(viewsets.ModelViewSet):
    """
    Gestione completa dei clienti:
    - GET /clients/ → list
    - POST /clients/ → add
    - GET /clients/<id>/ → detail
    - PUT /clients/<id>/ → update
    - DELETE /clients/<id>/ → delete
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class VehiculeViewSet(viewsets.ModelViewSet):
    """
    Gestione completa dei veicoli:
    - GET /vehicules/ → list
    - POST /vehicules/ → add
    - GET /vehicules/<id>/ → detail
    - PUT /vehicules/<id>/ → update
    - DELETE /vehicules/<id>/ → delete  
    - GET /clients/<client_id>/vehicules/ → list 
    - POST /clients/<client_id>/vehicules/ → add
    - GET /clients/<client_id>/vehicules/<id>/ → detail of a one vehicule associated to a client
    - POST /clients/<client_id>/vehicules/<id>/ → update 
    """
    queryset = Vehicule.objects.all()
    serializer_class = VehiculeSerializer

    def get_queryset(self):
        queryset = Vehicule.objects.all()

        client_id = self.kwargs.get('client_pk') #declared into the nested routes in urls.py in lookup
        if client_id:
            queryset = queryset.filter(owner_id=client_id)

        return queryset
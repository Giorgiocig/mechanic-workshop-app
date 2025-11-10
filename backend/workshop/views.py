from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from workshop.models import Client, Vehicule
from workshop.serializer import ClientSerializer, VehiculeSerializer

# Client Views
@api_view(["GET"])
def get_clients(request):
  clients=Client.objects.all()
  serialized_data=ClientSerializer(clients, many=True).data
  return Response(serialized_data)

@api_view(["POST"])
def create_client(request):
  data=request.data
  serializer=ClientSerializer(data=data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_client(request, pk):
  try:
    client=Client.objects.get(pk=pk)
  except Client.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  client.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["PUT"])
def update_client(request, pk):
  try:
    client=Client.objects.get(pk=pk)
  except Client.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  data=request.data
  serializer=ClientSerializer(client, data=data)
  if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Clients with vehicules
@api_view(["GET"])
def get_client_with_vehicules(request, pk):
    try:
        client = Client.objects.prefetch_related('veicoli').get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ClientSerializer(client)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_vehicule_for_client(request, client_id):
    try:
        client = Client.objects.get(pk=client_id)
    except Client.DoesNotExist:
        return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
    
    data = request.data.copy()
    data["owner"] = client.id 

    serializer = VehiculeSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


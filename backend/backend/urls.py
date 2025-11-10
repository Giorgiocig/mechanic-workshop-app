"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from workshop.views import create_client, get_clients, delete_client, update_client, get_client_with_vehicules

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', get_clients, name="get_clients"),          # GET
    path('clients/', create_client, name="create_client"),      # POST
    path('clients/<int:pk>/', update_client, name="update_client"),  # PUT
    path('clients/<int:pk>/', delete_client, name="delete_client"),   # DELETE
    path('clients/<int:pk>/', get_client_with_vehicules, name="get_client_with_vehicules") #GET CLIENTS WITH VEHICULES
]

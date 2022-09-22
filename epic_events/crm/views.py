from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from crm.serializers import ClientSerialiser
from crm.models import Client


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerialiser
    queryset = Client.objects.all()

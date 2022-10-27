from django.shortcuts import render
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from crm.serializers import (
    ClientSerialiser,
    ContractSerialiser,
    EventSerialiser,
)
from crm.models import Client, Contract, Event
from crm.permissions import ClientPermission


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerialiser
    permission_classes = [IsAuthenticated, ClientPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['compagny_name', 'email']

    def get_queryset(self):
        if self.request.user.team == 'sales':
            no_clients = Client.objects.filter(is_client=False)
            clients = Client.objects.filter(sales_contact=self.request.user)
            return no_clients | clients

        elif self.request.user.team == 'support':
            return Client.objects.filter(
                contractclient__contract__support_contact=self.request.user
            )
        return Client.objects.all()

    def perform_create(self, serializer):
        if self.request.data['is_client'] == 'true':
            serializer.save(sales_contact=self.request.user)
        else:
            serializer.save()

    def perform_update(self, serializer):
        if self.request.data['is_client'] == 'true':
            serializer.save(sales_contact=self.request.user)

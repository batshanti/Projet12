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


class EventViewset(ModelViewSet):
    serializer_class = EventSerialiser
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['compagny_name', 'email', 'event_date']

    def get_queryset(self):
        if self.request.user.team == 'sales':
            clients = Event.objects.filter(sales_contact=self.request.user)
            ids_clients = []
            for client in clients:
                ids_clients.append(client.id)
            return Event.objects.filter(id__in=client.id)
        elif self.request.user.team == 'support':
            return Event.objects.filter(support_contact=self.request.user)

        return Event.objects.all()

    def perform_create(self, serializer):
        contract = Contract.objects.get(pk=self.request.data['contract'])
        serializer.save(client=contract.client)

from django.shortcuts import render
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from crm.serializers import ClientSerialiser, ContractSerialiser, EventSerialiser
from crm.models import Client, Contract, Event


class ClientViewset(ModelViewSet):
    serializer_class = ClientSerialiser
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['compagny_name', 'email']

    def get_queryset(self):
        if self.request.user.team == 'sales':
            no_clients = Client.objects.filter(is_client=False)
            clients = Client.objects.filter(sales_contact=self.request.user)

            return no_clients | clients

        elif self.request.user.team == 'support':

            return Client.objects.filter(event__support_contact=self.request.user)
            # support_clients_ids = Event.objects.filter(
            #     support_contact=self.request.user
            # )
            # ids_clients = []
            # for client in support_clients_ids:
            #     ids_clients.append(client.client.id)
            # return Client.objects.filter(id__in=ids_clients)

        return Client.objects.all()

    def perform_create(self, serializer):
        if self.request.data['is_client'] == 'true':
            serializer.save(sales_contact=self.request.user)

    def perform_update(self, serializer):
        if self.request.data['is_client'] == 'true':
            serializer.save(sales_contact=self.request.user)


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerialiser
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['compagny_name', 'email', 'date_created', 'amount']


    def get_queryset(self):
        if self.request.user.team == 'sales':
            return Contract.objects.filter(sales_contact=self.request.user)
        elif self.request.user.team == 'support':
            return Contract.objects.filter(Event__support_contact=self.request.user)
            # support_clients_ids = Event.objects.filter(
            #     support_contact=self.request.user
            # )
            # ids_clients = []
            # for client in support_clients_ids:
            #     ids_clients.append(client.client.id)
            # return Contract.objects.filter(id__in=ids_clients)

        return Contract.objects.all()

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


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

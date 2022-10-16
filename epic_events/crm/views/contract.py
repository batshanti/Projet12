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


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerialiser
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['compagny_name', 'email', 'date_created', 'amount']

    def get_queryset(self):
        if self.request.user.team == 'sales':
            return Contract.objects.filter(sales_contact=self.request.user)
        elif self.request.user.team == 'support':
            return Contract.objects.filter(
                Event__support_contact=self.request.user
            )
        return Contract.objects.all()

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)
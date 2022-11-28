from django_filters.rest_framework import DjangoFilterBackend
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
from crm.permissions import ContractPermission


class ContractViewset(ModelViewSet):
    serializer_class = ContractSerialiser
    permission_classes = [IsAuthenticated, ContractPermission]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['compagny_name', 'email', 'date_created', 'amount']
    filterset_fields = ['status']

    def get_queryset(self):
        if self.request.user.team == 'sales':
            return Contract.objects.filter(sales_contact=self.request.user)
        elif self.request.user.team == 'support':
            return Contract.objects.filter(
                event__support_contact=self.request.user
            )
        else:
            return Contract.objects.all()

    def perform_create(self, serializer):
        serializer.save(sales_contact=self.request.user)


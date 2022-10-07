from crm.models import Client, Contract, Event
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class ClientSerialiser(ModelSerializer):

    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ['sales_contact']


class ContractSerialiser(ModelSerializer):

    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ['sales_contact']


class EventSerialiser(ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ['support_contact']

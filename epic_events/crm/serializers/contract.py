from crm.models import Client, Contract, Event
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class ContractSerialiser(ModelSerializer):

    class Meta:
        model = Contract
        fields = "__all__"
        read_only_fields = ['sales_contact']

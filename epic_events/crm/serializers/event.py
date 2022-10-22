from crm.models import Client, Contract, Event
from rest_framework.serializers import ModelSerializer, SerializerMethodField


class EventSerialiser(ModelSerializer):

    class Meta:
        model = Event
        fields = "__all__"
        read_only_fields = ['support_contact']

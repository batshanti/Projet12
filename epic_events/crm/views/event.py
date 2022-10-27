from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from crm.serializers import EventSerialiser
from crm.models import Event
from crm.permissions import EventPermission


class EventViewset(ModelViewSet):
    serializer_class = EventSerialiser
    permission_classes = [IsAuthenticated, EventPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['compagny_name', 'email', 'event_date']

    def get_queryset(self):
        if self.request.user.team == 'sales':
            return Event.objects.filter(
                contract__sales_contact=self.request.user
            )
        elif self.request.user.team == 'support':
            return Event.objects.filter(support_contact=self.request.user)

        return Event.objects.all()

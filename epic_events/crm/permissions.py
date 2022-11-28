from rest_framework.permissions import BasePermission, SAFE_METHODS
from crm.models import Client, Contract


class ClientPermission(BasePermission):

    def has_permission(self, request, view):

        if view.action in ['create', 'update']:
            if request.user.team == 'sales':
                return True
        else:
            return True

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return request.user
        elif request.method in ['PATCH', 'DELETE']:
            if not obj.is_client:
                return request.user.team == 'sales'
            else:
                return request.user == obj.sales_contact


class ContractPermission(BasePermission):

    def has_permission(self, request, view):

        if view.action == 'create':
            client = Client.objects.get(pk=request.data['client'])
            if request.user == client.sales_contact:
                return True
        else:
            return True

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return request.user
        elif request.method in ['PATCH', 'DELETE']:
            if request.user == obj.sales_contact:
                return True
            else:
                return False


class EventPermission(BasePermission):

    def has_permission(self, request, view):

        if view.action == 'create':
            contract = Contract.objects.get(pk=request.data['contract'])
            client = Client.objects.get(pk=contract.client.id)
            if request.user == client.sales_contact:
                return True
        else:
            return True

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return request.user
        elif request.method == 'PATCH':
            if request.user == obj.support_contact and obj.status !='finished':
                return True
            else:
                return False

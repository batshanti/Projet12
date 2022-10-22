from rest_framework.permissions import BasePermission, SAFE_METHODS
from crm.models import Client


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
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
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
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            if request.user == obj.sales_contact:
                return True
            else:
                return False


class EventPermission(BasePermission):

    def has_permission(self, request, view):

        if view.action == 'create':
            if request.user.team == 'sales':
                return True
        else:
            return True

    def has_object_permission(self, request, view, obj):
        pass















        # print(obj.support_contact.id)
        # print(request.data['support_contact'])
        # print(view.data['support_contact'])
        # if request.method in ['PUT', 'PATCH']:
        #     if obj.support_contact.id == request.data['support_contact']:
        #         return True
        #     else:
        #         return False


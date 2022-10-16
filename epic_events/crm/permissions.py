from rest_framework.permissions import BasePermission, SAFE_METHODS


class ClientPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.team == 'support' or request.user.team == 'manager':
            return False
        return request.user.team == 'sales'

        # if view.action in ['create', 'update']:
        #     if request.user.team == 'sales':
        #         return True
        #     else:
        #         return False

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return request.user
        elif request.method in ['PUT', 'PATCH', 'DELETE']:
            return request.user == obj.sales_contact


class ContractPermission(BasePermission):
    pass


class EventPermission(BasePermission):
    pass

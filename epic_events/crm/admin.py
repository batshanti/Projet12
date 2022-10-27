from django.contrib import admin
from crm.models import Client, Event, Contract


class ClientAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_name',
        'last_name',
        'compagny_name',
        'email',
        'sales_contact',
        'is_client'
    )
    search_fields = ('email',)


class ContractAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'sales_contact',
        'client',
        'status',
        'amount'
    )


class EventAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'support_contact',
        'attendees',
        'event_date',
        'status',
        'note'
    )


admin.site.register(Client, ClientAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Contract, ContractAdmin)



# class UserAdmin(admin.ModelAdmin):
# admin.site.register(User, UserAdmin)
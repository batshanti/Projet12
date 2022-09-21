from django.contrib import admin
from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'team')

    fieldsets = (
        (
            'User information',
            {'fields': (
                'username',
                'first_name',
                'last_name',
                'email',
                'password',
                'team'
            )}
        ),
    )
    search_fields = ('email',)


admin.site.register(User, UserAdmin)

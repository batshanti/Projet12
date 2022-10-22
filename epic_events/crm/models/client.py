from django.db import models
from django.conf import settings


class Client(models.Model):

    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=16)
    mobile = models.CharField(max_length=16)
    compagny_name = models.CharField(max_length=256)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'team': 'sales'},
    )
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.compagny_name}'

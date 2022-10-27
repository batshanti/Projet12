from django.db import models
from django.conf import settings
from crm.models import Client


class Contract(models.Model):

    sales_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        limit_choices_to={'team': 'sales'},
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        limit_choices_to={'is_client': True},
        related_name='contractclient'
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name='Signed')
    amount = models.FloatField()
    payment_due = models.DateTimeField()

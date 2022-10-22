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
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False, verbose_name='Signed')
    amount = models.FloatField()
    payment_due = models.DateTimeField()


class Event(models.Model):

    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        related_name='contract',
        limit_choices_to={'status': 'True'}
    )
    client = models.ForeignKey(
        Client,
        limit_choices_to={'is_client': True},
        on_delete=models.CASCADE,
        related_name='event',
        blank=True
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    support_contact = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'team': 'support'},
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    attendees = models.IntegerField()
    event_date = models.DateTimeField()
    note = models.TextField()

    def __str__(self):
        return f'{self.event_date} - {self.client}'

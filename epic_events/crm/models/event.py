from django.db import models
from django.conf import settings
from crm.models import Contract

STATUS = [
    ('in_progress', 'in_progress'),
    ('finished', 'finished')
]


class Event(models.Model):

    contract = models.OneToOneField(
        Contract,
        on_delete=models.CASCADE,
        related_name='contract',
        limit_choices_to={'status': 'True'}
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
    status = models.CharField(
        max_length=12,
        choices=STATUS,
        blank=False,
        default='in_progress'
    )
    note = models.TextField()

    def __str__(self):
        return f'{self.event_date} - {self.contract}'

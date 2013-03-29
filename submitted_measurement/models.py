from django.db import models
from django.utils import timezone


class SubmittedMeasurement(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date of measurement', default=timezone.now)
    user = models.CharField(max_length=100)
    tags = []

    def __unicode__(self):
        return str(self.id)


class Choices(models.Model):
    ALL_CHOICES = (
        (0, 'None'),
        (1, 'Transaction type'),
        (2, 'Scaling factor'),
        (3, 'Number of threads'),
        (4, 'Number of clients'),
        (5, 'Number of transactions per client'),
        (6, 'Number of transactions actually processed'),
        (7, 'Transactions per second (including connections establishing)'),
        (8, 'Transactions per second (excluding connections establishing)'),
        (9, '*Special field ...')
    )
    name = models.CharField(max_length=100)
    all_choices = models.PositiveSmallIntegerField(default=0, choices=ALL_CHOICES)
    user = models.CharField(max_length=100)


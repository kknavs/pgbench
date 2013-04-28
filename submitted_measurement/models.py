from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.contrib import admin


class SubmittedMeasurement(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date of measurement', default=timezone.now)
    user = models.ForeignKey(User)
    #tags = []
    tags = models.CharField(max_length=150, blank=True)

    def __unicode__(self):
        return unicode(self.id)


class SubmittedMeasurementAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date')
    list_filter = ('user', 'date')


class SubmittedMeasurementForm(forms.ModelForm):
    class Meta:
        model = SubmittedMeasurement
        exclude = 'user'


class Choice(models.Model):
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


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
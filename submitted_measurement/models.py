from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.contrib import admin


class SubmittedMeasurement(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date of measurement', default=timezone.now)
    user = models.ForeignKey(User)
    tags = models.CharField(max_length=150, blank=True)
    transactionType = models.CharField(max_length=150, blank=True)
    scalingFactor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    threads = models.IntegerField(max_length=30, blank=True, null=True)
    clients = models.IntegerField(max_length=30, blank=True, null=True)
    transactionsPerClient = models.IntegerField(max_length=30, blank=True, null=True)
    transactions = models.IntegerField(max_length=30, blank=True, null=True)
    TPS = models.IntegerField(max_length=30, blank=True, null=True)
    TPSConnEstablish = models.IntegerField(max_length=30)

    def __unicode__(self):
        return unicode(self.id)


class SubmittedMeasurementAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date')
    list_filter = ('user', 'date')


class SubmittedMeasurementForm(forms.ModelForm):
    class Meta:
        model = SubmittedMeasurement
        exclude = 'user'

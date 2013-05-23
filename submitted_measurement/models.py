from django.db import models
from django.utils import timezone
from django import forms
from django.contrib.auth.models import User
from django.contrib import admin


class SubmittedMeasurement(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date of measurement', default=timezone.now)
    user = models.ForeignKey(User)
    tags = models.CharField(max_length=150)
    TPSConnEstablish = models.IntegerField(max_length=30)
    transactionType = models.CharField('transaction type',
                                       max_length=150, blank=True)
    scalingFactor = models.DecimalField(max_digits=5, decimal_places=2,
                                        blank=True, null=True)
    threads = models.IntegerField(max_length=30, blank=True, null=True)
    clients = models.IntegerField(max_length=30, blank=True, null=True)
    transactionsPerClient = models.IntegerField(
        'Transactions per client', max_length=30, blank=True, null=True)
    transactions = models.IntegerField(max_length=30,
                                       blank=True, null=True)
    TPS = models.IntegerField(max_length=30,
                              blank=True, null=True)

    def __unicode__(self):
        return unicode(self.id)


class SubmittedMeasurementAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'transactionType',
                    'scalingFactor', 'threads', 'clients',
                    'transactionsPerClient', 'transactions',
                    'TPS', 'TPSConnEstablish')
    list_filter = ('user', 'date')


class SubmittedMeasurementForm(forms.ModelForm):
    class Meta:
        model = SubmittedMeasurement
        exclude = 'user'


class Fields(models.Model):
    measure = models.ForeignKey(SubmittedMeasurement)
    name = models.CharField(max_length=100, blank=True, null=True)
    typeOf = models.CharField(max_length=30, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.name + ": " + self.value)


class FieldsForm(forms.ModelForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        cd = cleaned_data
        str_list = filter(bool, cd.values())
        if 0 < len(str_list) < len(cd):
            raise forms.ValidationError(
                "All fields of one 'Special field' "
                "must be filled up or left empty.")
            # Always return the full collection of cleaned data.
        return cd

    class Meta:
        model = Fields
        exclude = 'measure'


class UploadForm(forms.Form):
    upload = forms.FileField(
        label='Select a file (must be in .csv format)',
    )

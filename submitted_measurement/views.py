import os
from submitted_measurement.models import *
from django.shortcuts import render
from django import http
from django.contrib import messages
from submitted_measurement import insertData
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings


def contact(request):
    model_form = SubmittedMeasurementForm
    model_formF = FieldsForm
    upload_form = UploadForm
    if request.user.is_authenticated and request.method == 'POST':
        form = model_form(request.POST)
        formF = model_formF(request.POST)
        upload = UploadForm(request.POST, request.FILES)
        if form.is_valid() and formF.is_valid():
            title = form.cleaned_data.get('title')
            date = form.cleaned_data['date']
            tags = form.cleaned_data['tags']
            TPSConnEst = form.cleaned_data['TPSConnEstablish']
            transT = form.cleaned_data['transactionType']
            scaling = form.cleaned_data['scalingFactor']
            threads = form.cleaned_data['threads']
            clients = form.cleaned_data['clients']
            transC = form.cleaned_data['transactionsPerClient']
            trans = form.cleaned_data['transactions']
            TPS = form.cleaned_data['TPS']
            sm = SubmittedMeasurement(
                user=request.user, title=title, date=date, tags=tags,
                TPSConnEstablish=TPSConnEst, transactionType=transT,
                scalingFactor=scaling, threads=threads, clients=clients,
                transactionsPerClient=transC, transactions=trans, TPS=TPS)
            sm.save()
            cd = formF.cleaned_data
            if cd.get('name'):
                ff = Fields(measure=sm, name=cd.get('name'),
                            typeOf=cd.get('typeOf'), value=cd.get('value'))
                ff.save()
            messages.add_message(request, messages.INFO, "Successful!")
            return http.HttpResponseRedirect('')
        elif upload.is_valid():
            data = request.FILES['upload']
            name = data.name
            if name.split(".")[1].lower() == "csv":
                path = default_storage.save('temp/'+name, ContentFile(data.read()))
                path = settings.MEDIA_ROOT+path
                if insertData.test(path):
                    messages.add_message(request, messages.INFO, "Successful!")
                    os.remove(path)
            else:
                messages.add_message(request, messages.INFO, "Wrong file format")
            return http.HttpResponseRedirect('')
    else:
        form = model_form()
        formF = model_formF()
        upload = upload_form()

    return render(request, 'submit.html', {
        'form': form, 'fieldsForm': formF, 'uploadForm': upload
    })


def get(request):
    return render(request, 'analyze.html')


def search(request):
    return render(request, 'search.html')

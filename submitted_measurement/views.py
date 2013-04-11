from submitted_measurement.models import SubmittedMeasurement, SubmittedMeasurementForm
from django.shortcuts import render


def contact(request):
    model_form = SubmittedMeasurementForm
    if request.method == 'POST':
        form = model_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            username = form.cleaned_data['user']
            date = form.cleaned_data['date']
            sm = SubmittedMeasurement(user=username, title=title, date=date)
            sm.save()
            return render(request, 'submit.html', {
                'form': form, 'confirm': True
            })
    else:
        form = model_form()

    return render(request, 'submit.html', {
        'form': form,
    })


def get(request):
    sm = SubmittedMeasurement.objects.all()
    return render(request, 'analyze.html', {'measures': sm})

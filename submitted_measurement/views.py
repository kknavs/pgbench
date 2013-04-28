from submitted_measurement.models import SubmittedMeasurement, SubmittedMeasurementForm, Choice
from django.shortcuts import render


def contact(request):
    model_form = SubmittedMeasurementForm
    if request.user.is_authenticated and request.method == 'POST':
        form = model_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            date = form.cleaned_data['date']
            tags = form.cleaned_data['tags']
            sm = SubmittedMeasurement(user=request.user, title=title, date=date, tags=tags)
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
    return render(request, 'analyze.html')

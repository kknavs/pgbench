from django.contrib import admin
from submitted_measurement.models import *

admin.site.register(SubmittedMeasurement, SubmittedMeasurementAdmin)

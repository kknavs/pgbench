# myapp/api.py
from tastypie.resources import ModelResource
from submitted_measurement.models import SubmittedMeasurement


class MeasuresResource(ModelResource):
    class Meta:
        queryset = SubmittedMeasurement.objects.all()
        resource_name = 'measures'


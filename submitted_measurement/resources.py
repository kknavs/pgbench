# myapp/api.py
from tastypie.resources import ModelResource
from submitted_measurement.models import SubmittedMeasurement
from django.contrib.auth.models import User
from tastypie import fields


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'last_login']
        allowed_methods = ['get']

    # called every time when object is prepared for serialization
    def dehydrate(self, bundle):
        return bundle.data['username']


class MeasuresResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)

    class Meta:
        queryset = SubmittedMeasurement.objects.all()
        resource_name = 'measures'
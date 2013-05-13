# myapp/api.py
from tastypie.resources import ModelResource
from submitted_measurement.models import SubmittedMeasurement, Fields
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
        if bundle.request.user.pk == bundle.obj.pk:
            return bundle.data["username"]

    def get_object_list(self, request):
        if request and not request.user.pk is None:
            return super(UserResource, self).\
                get_object_list(request).filter(pk=request.user.pk)
        return SubmittedMeasurement.objects.get_empty_query_set()


class MeasuresResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)

    class Meta:
        queryset = SubmittedMeasurement.objects.all()
        resource_name = 'measures'
        allowed_methods = ['get']

    def hydrate_user(self, bundle):
        if not bundle.request.user.pk == bundle.obj.pk:
            bundle.data['user'] = -1
        else:
            bundle.data['user'] = bundle.obj.user.pk
        return bundle

    def dehydrate(self, bundle):  # FieldsResource?
        l = list(Fields.objects.filter(measure=bundle.data['id']))
        if l:
            bundle.data['fields'] = l
        else:
            bundle.data['fields'] = '/'
        return bundle

    def get_object_list(self, request):
        if request and not request.user.pk is None:
            return super(MeasuresResource, self)\
                .get_object_list(request).filter(user=request.user.pk)
        return SubmittedMeasurement.objects.get_empty_query_set()

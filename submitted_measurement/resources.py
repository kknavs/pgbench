# myapp/api.py
from tastypie.resources import ModelResource
from submitted_measurement.models import SubmittedMeasurement, Fields
from django.contrib.auth.models import User
from tastypie import fields
from django.core.paginator import Paginator, InvalidPage
from django.http import Http404
from django.conf.urls import *
from tastypie.utils import trailing_slash


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

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search%s$" % (self._meta.resource_name,
                trailing_slash()), self.wrap_view('get_search'),
                name="api_get_search"),
        ]

    def get_object_list(self, request):
        if request and not request.user.pk is None:
            return super(MeasuresResource, self)\
                .get_object_list(request).filter(user=request.user.pk)
        return SubmittedMeasurement.objects.get_empty_query_set()

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)
        q = ''
        if 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
        # Do the query.
        sqs = super(MeasuresResource, self)\
            .get_object_list(request).filter(title__icontains=q, user=request.user.pk)
        paginator = Paginator(sqs, 20)

        try:
            page = paginator.page(int(request.GET.get('page', 1)))
        except InvalidPage:
            raise Http404("Sorry, no results on that page.")

        objects = []

        for result in page.object_list:
            bundle = self.build_bundle(obj=result, request=request)
            bundle = self.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)

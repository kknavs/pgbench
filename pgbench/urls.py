from django.conf.urls import patterns, url, include
from pgbench.frontend import views as frontend_views
from pgbench.users import views as user_views
from submitted_measurement import views as measure_views
from django.views.defaults import server_error, page_not_found
from django.utils.functional import curry
from tastypie.api import Api
from submitted_measurement.resources import MeasuresResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(MeasuresResource())
v1_api.register(UserResource())

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', frontend_views.HomeView.as_view(), name='home'),
    url(r'^search/$', measure_views.search),
    url(r'^submit/$', measure_views.contact, name="submitM"),
    url(r'^analyze/$', measure_views.get),
    url(r'^register/$',
        user_views.RegisterView.as_view(template_name='users/register.html')),
    url(r'^login/$',
        user_views.LoginView.as_view(template_name='users/login.html')),
    url(r'^logout/$', user_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),
    #http://127.0.0.1:8000/api/v1/measures/?format=json
)

handler404 = curry(page_not_found, template_name='404.html')
handler500 = curry(server_error, template_name='500.html')

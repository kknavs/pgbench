from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from pgbench.frontend import views as frontend_views
from pgbench.users import views as user_views
from submitted_measurement import views as measure_views
from django.views.defaults import server_error, page_not_found
from django.utils.functional import curry

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', frontend_views.HomeView.as_view(), name='home'),
                       url('^search/$', TemplateView.as_view(template_name="search.html")),
                       url('^submit/$', measure_views.contact, name="submitM"),
                       url('^analyze/$', measure_views.get, name="show"),
                       url('^register/$', user_views.RegisterView.as_view(template_name='users/register.html')),
                       url('^login/$', user_views.LoginView.as_view(template_name='users/login.html')),
                       url('^logout/$', user_views.LogoutView.as_view(), name='logout'),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)

handler404 = curry(page_not_found, template_name='404.html')
handler500 = curry(server_error, template_name='500.html')
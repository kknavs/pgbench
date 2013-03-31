from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from pgbench.frontend import views as frontend_views
from pgbench.users import views as user_views
from submitted_measurement import views as measure_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', frontend_views.HomeView.as_view(), name='home'),
                       url('^search/$', TemplateView.as_view(template_name="search.html")),
                       url('^submit/$', TemplateView.as_view(template_name="submit.html")),
                       url('^analyze/$', TemplateView.as_view(template_name="analyze.html")),
                       url('^register/$', user_views.RegisterView.as_view(template_name='users/register.html')),
                       url('^login/$', user_views.LoginView.as_view(template_name='users/login.html')),
                       url('^logout/$', user_views.LogoutView.as_view(), name='logout'),
                       url(r'^admin/', include(admin.site.urls)),
)
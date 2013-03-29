from django.conf.urls import patterns
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('pgbench.frontend.views',
                       (r'^$', 'home_view'),
                       ('^search/', TemplateView.as_view(template_name="search.html")),
                       ('^submit/', TemplateView.as_view(template_name="submit.html")),
                       )

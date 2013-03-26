from django.conf.urls import patterns, url
from pgbench.frontend import views as frontend_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('pgbench.frontend.views',
                       ('^$', 'home_view'),

)

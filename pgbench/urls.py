from django.conf.urls import patterns, url
from pgbench.frontend import views as frontend_views
from pgbench.users import views as user_views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('pgbench.frontend.views',
                       ('^$', 'home_view'),
)

urlpatterns += patterns('pgbench.users.views',
                        url('^login$', user_views.RegisterView.as_view(), name='registration'),
                        ('^register$', 'register'),
)



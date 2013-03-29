# Create your views here.

from django.shortcuts import render_to_response
from django.views import generic as generic_views


class HomeView(generic_views.TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        return super(HomeView, self).get(request, *args, **kwargs)


from django.shortcuts import render_to_response
from django.views import generic as generic_views
from pgbench.users import forms


def login(request):
    form_class = forms.LoginForm
    return render_to_response('users/login.html')


class RegisterView(generic_views.FormView):
    template_name = 'users/register.html'
    form_class = forms.UserRegistationForm

    def get(self, request, *args, **kwargs):
        return super(RegisterView, self).get(request, *args, **kwargs)

from django.contrib.auth import authenticate, login, logout
from django.core import urlresolvers
from django.views import generic as generic_views
from pgbench.users import forms
from django.shortcuts import redirect
from django.contrib.auth.models import User


class LoginView(generic_views.FormView):
    template_name = 'login.html'
    form_class = forms.LoginForm
    success_url = urlresolvers.reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class LogoutView(generic_views.RedirectView):

    def get(self, request, *args, **kwargs):
        logout(self.request)
        return redirect('/')


class RegisterView(generic_views.FormView):
    template_name = 'register.html'
    form_class = forms.UserRegistationForm
    success_url = urlresolvers.reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return super(RegisterView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']

        user = User(username=username, email=email,)
        user.set_password(password)
        user.save()

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)






from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from .forms import RegisterUserForm, LoginUserForm


class RegisterUserView(FormView):
    """
    Register as a user, provide username, email and password
    """
    template_name = 'auth_ex/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password']
        )
        return super().form_valid(form)


class LoginUserView(FormView):
    """
    Allows to login as a user with a username and password
    """
    template_name = 'auth_ex/login.html'
    form_class = LoginUserForm

    def form_valid(self, form):
        request = self.request
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(request, user)
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', reverse_lazy('index'))


class LogoutUserView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'auth_ex/logout.html')

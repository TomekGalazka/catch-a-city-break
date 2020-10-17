from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView

from .forms import RegisterUserForm, LoginUserForm


class RegisterUserView(FormView):
    template_name = 'auth_ex/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']

        if password == repeat_password:
            user = User.objects.create_user(username=username, email=email, password=password)
        return super().form_valid(form)


class LoginUserView(FormView):
    template_name = 'auth_ex/login.html'
    form_class = LoginUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        request = self.request
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(request, user)
        return super().form_valid(form)


class LogoutUserView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'auth_ex/logout.html')

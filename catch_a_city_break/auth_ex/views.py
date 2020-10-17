from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import RegisterUserForm


class RegisterUserView(FormView):
    template_name = 'auth_ex/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('city_breaks_app:index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']

        if password == repeat_password:
            user = User.objects.create_user(username=username, email=email, password=password)

        return super().form_valid(form)
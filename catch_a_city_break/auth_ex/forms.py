from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from django import forms


User = get_user_model()


class RegisterUserForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data['username']
        email = cleaned_data['email']
        password = cleaned_data['password']
        repeat_password = cleaned_data['repeat_password']

        users = User.objects.all()

        if password != repeat_password:
            raise ValidationError('Your password does not match. Please repeat the password correctly.')

        for user in users:
            if username == user.username:
                raise ValidationError('This user already exists. Please choose another name.')

        if '@' not in email:
            raise ValidationError('Please provide a valid e-mail address.')


class LoginUserForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data['username']
        password = cleaned_data['password']

        if authenticate(username=username, password=password) is None:
            raise ValidationError('Your username or password is incorrect.')


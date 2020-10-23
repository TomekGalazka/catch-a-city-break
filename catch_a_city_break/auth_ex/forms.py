from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ValidationError
from django import forms


User = get_user_model()


class RegisterUserForm(forms.Form):
    """
    Form to create a new user.
    """
    username = forms.CharField(label='Username:')
    email = forms.EmailField(widget=forms.EmailInput, label='E-mail:')
    password = forms.CharField(widget=forms.PasswordInput, label='Password:')
    repeat_password = forms.CharField(widget=forms.PasswordInput, label='Repeat Password:')

    username.widget.attrs.update({'class': 'form-control mb-3'})
    email.widget.attrs.update({'class': 'form-control mb-3'})
    password.widget.attrs.update({'class': 'form-control mb-3'})
    repeat_password.widget.attrs.update({'class': 'form-control mb-3'})

    def clean(self):
        """
        Overwrite clean method to check if there are any errors.
        :return: ValidationError, if there is any.
        """
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

        if '@' and '.' not in email:
            raise ValidationError('Please provide a valid e-mail address.')


class LoginUserForm(forms.Form):
    """
    Form to login existing user.
    """
    username = forms.CharField(label='Username:')
    password = forms.CharField(widget=forms.PasswordInput, label='Password:')

    username.widget.attrs.update({'class': 'form-control mb-3'})
    password.widget.attrs.update({'class': 'form-control mb-3'})

    def clean(self):
        """
        Overwrite clean method to check if there are any errors.
        :return: ValidationError, if user is not authenticated.
        """
        cleaned_data = super().clean()
        username = cleaned_data['username']
        password = cleaned_data['password']

        if authenticate(username=username, password=password) is None:
            raise ValidationError('Your username or password is incorrect.')


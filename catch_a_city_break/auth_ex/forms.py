from django import forms


class RegisterUserForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)


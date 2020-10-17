from django.urls import path

from . import views


app_name = 'auth_ex'

urlpatterns = [
    path('register_user/', views.RegisterUserView.as_view(), name='register-user'),

]

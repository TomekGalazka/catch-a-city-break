from django.urls import path

from . import views


app_name = 'auth_ex'

urlpatterns = [
    path('register_user/', views.RegisterUserView.as_view(), name='register-user'),
    path('login_user/', views.LoginUserView.as_view(), name='login-user'),
    path('logout_user/', views.LogoutUserView.as_view(), name='logout-user'),

]

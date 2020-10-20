"""catch_a_city_break URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from city_breaks_app import views as CityBreakView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CityBreakView.IndexView.as_view(), name='index'),
    path('city-breaks/', include('city_breaks_app.urls')),
    path('auth/', include('auth_ex.urls')),
    path(
        'destinations_activity_types/',
        CityBreakView.DestinationsActivitiesView.as_view(),
        name='destination-activities'
    ),
    path('about/', CityBreakView.AboutView.as_view(), name='about'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
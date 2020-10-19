from django.contrib import admin

from city_breaks_app.models import Activities


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "duration", "city", "activity_type", 'image')

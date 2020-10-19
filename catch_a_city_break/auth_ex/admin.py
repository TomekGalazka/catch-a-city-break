from django.contrib import admin

from city_breaks_app.models import Activities, WeekDay


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "duration", "city", "activity_type", 'image')


@admin.register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    list_display = ("name", "order")

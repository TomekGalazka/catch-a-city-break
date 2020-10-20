from django.contrib import admin

from city_breaks_app.models import Activities, WeekDay, TravelPlan


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "duration", "city", "activity_type", 'image')


@admin.register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    list_display = ("name", "order")


@admin.register(TravelPlan)
class TravelPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "created", "user")

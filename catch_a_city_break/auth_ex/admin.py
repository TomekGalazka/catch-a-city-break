from django.contrib import admin

from city_breaks_app.models import Activities, WeekDay, TravelPlan


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    """
    Allows to modify Actvities model in admin panel.
    """
    list_display = ("name", "description", "duration", "city", "activity_type", 'image')


@admin.register(WeekDay)
class WeekDayAdmin(admin.ModelAdmin):
    """
    Allows to modify WeekDay model in admin panel.
    """
    list_display = ("name", "order")


@admin.register(TravelPlan)
class TravelPlanAdmin(admin.ModelAdmin):
    """
    Allows to modify TravelPlan model in admin panel.
    """
    list_display = ("name", "description", "created", "user")

from django.urls import path

from . import views

app_name = 'city_breaks_app'

urlpatterns = [
    path('create_travel_plan/', views.TravelPlanCreateView.as_view(), name='travel-plan-create'),
    path('travel_plans/', views.TravelPlansView.as_view(), name='travel-plans'),
    path('travel_plan_details/<int:plan_id>/', views.TravelPlanDetailView.as_view(), name='travel-plan-details'),

]

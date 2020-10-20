from django.urls import path

from . import views

app_name = 'city_breaks_app'

urlpatterns = [
    path('create_travel_plan/', views.TravelPlanCreateView.as_view(), name='travel-plan-create'),
    path('travel_plans/', views.TravelPlansView.as_view(), name='travel-plans'),
    path('travel_plan_details/<int:plan_id>/', views.TravelPlanDetailView.as_view(), name='travel-plan-details'),
    path('select_activity/', views.ActivitySelectView.as_view(), name='select-activity'),
    path('add_activity_to_plan/<int:activity_id>', views.AddActivityToPlanView.as_view(), name='add-activity-to-plan'),
    path('activities_detail/<int:pk>/', views.ActivityDetailsView.as_view(), name='activities-detail'),
    path('ask_for_offer/', views.AskForOfferView.as_view(), name='ask-for-offer'),

]

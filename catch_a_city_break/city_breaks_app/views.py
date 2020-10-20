from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy, reverse

from .forms import ActivitySelectForm, AddActivityToPlan
from .models import TravelPlan, Activities, TravelPlanActivities, WeekDay


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class DestinationsActivitiesView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'destinations_activity_types.html')


class TravelPlanCreateView(LoginRequiredMixin, CreateView):
    model = TravelPlan
    fields = ['name', 'description']
    login_url = '/auth/login_user/'
    success_url = reverse_lazy('city_breaks_app:travel-plans')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TravelPlansView(View):
    def get(self, request, *args, **kwargs):
        user = request.user
        ctx = {}
        if user.is_authenticated:
            plans = TravelPlan.objects.filter(user=user)
            ctx = {'plans': plans}
            return render(request, 'city_breaks_app/travel_plans.html', ctx)
        else:
            return render(request, 'city_breaks_app/travel_plans.html', ctx)


class TravelPlanDetailView(LoginRequiredMixin, View):
    login_url = reverse_lazy('auth_ex:login-user')

    def get(self, request, *args, **kwargs):
        user = request.user
        ctx = {}
        if user.is_authenticated:
            plan = TravelPlan.objects.get(pk=kwargs['plan_id'])
            plan_activities = plan.travelplanactivities_set.all().order_by('week_day', 'time')
            ctx = {
                'plan': plan,
                'plan_activities': plan_activities
            }
            return render(request, 'city_breaks_app/travel_plan_details.html', ctx)
        else:
            return render(request, 'city_breaks_app/travel_plan_details.html', ctx)


class ActivitySelectView(LoginRequiredMixin, View):
    login_url = reverse_lazy('auth_ex:login-user')

    def get(self, request, *args, **kwargs):
        form = ActivitySelectForm()
        return render(request, 'city_breaks_app/select_activity.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ActivitySelectForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            activity_type = form.cleaned_data['activity_type']
            selected_activities = Activities.objects.filter(city=city, activity_type=activity_type)
            ctx = {
                'form': form,
                'selected_activities': selected_activities
            }
            return render(request, 'city_breaks_app/select_activity.html', ctx)
        else:
            return render(request, 'city_breaks_app/select_activity.html', {'form': form})


class AddActivityToPlanView(LoginRequiredMixin, View):
    login_url = reverse_lazy('auth_ex:login-user')

    def get(self, request, *args, **kwargs):
        chosen_activity_id = kwargs['activity_id']
        form = AddActivityToPlan(user=request.user, activity_id=chosen_activity_id)
        ctx = {
            'form': form,
            'chosen_activity': chosen_activity_id
        }
        return render(request, 'city_breaks_app/add_activity_to_plan.html', ctx)

    def post(self, request, *args, **kwargs):
        chosen_activity_id = kwargs['activity_id']
        form = AddActivityToPlan(request.POST, user=request.user, activity_id=chosen_activity_id)
        chosen_activity = Activities.objects.get(pk=chosen_activity_id)
        if form.is_valid():
            user = request.user
            travel_plan = form.cleaned_data['travel_plan']
            week_day_name = form.cleaned_data['week_day']
            time = form.cleaned_data['time']

            week_day = WeekDay.objects.get(name=week_day_name)

            register_activity = TravelPlanActivities.objects.create(
                travel_plan=travel_plan,
                activities=chosen_activity,
                week_day=week_day,
                time=time,
            )
            register_activity.user.add(user)
            return redirect(reverse('city_breaks_app:travel-plan-details', kwargs={'plan_id': travel_plan.pk}))
        else:
            return redirect(reverse('city_breaks_app:add-activity-to-plan', kwargs={'activity_id': chosen_activity_id}))


class ActivityDetails(LoginRequiredMixin, DetailView):
    model = Activities
    login_url = reverse_lazy('auth_ex:login-user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        activity_id = self.kwargs['pk']
        context['activity'] = Activities.objects.get(pk=activity_id)
        return context


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, FormView
from django.urls import reverse_lazy

from .forms import ActivitySelectForm
from .models import TravelPlan, Activities


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


class TravelPlanDetailView(View):
    def get(self, request, *args, **kwargs):
        plan = TravelPlan.objects.get(pk=kwargs['plan_id'])
        return render(request, 'city_breaks_app/travel_plan_details.html', {'plan': plan})


class ActivitySelectView(LoginRequiredMixin, View):
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

    # template_name = 'city_breaks_app/select_activity.html'
    # form_class = ActivitySelectForm
    # success_url = reverse_lazy('city_breaks_app:select-activity')

    # def form_valid(self, form):
    #     city = form.cleaned_data['city']
    #     activity_type = form.cleaned_data['activity_type']
    #     return super().form_valid(form)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['selected_activities'] = Activities.objects.filter(city=city, activity_type=activity_type)
    #     return context



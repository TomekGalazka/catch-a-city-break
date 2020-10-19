from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreateTravelPlanForm
from .models import TravelPlan


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


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


# class WhereDoYouGoView(FormView):
#     template_name = 'city_breaks_app/wheredoyougo.html'
#     form_class = WhereDoYouGoForm
#     success_url = reverse_lazy('city_breaks_app:destination_choice')
#
#     def form_valid(self, form):
#         pass

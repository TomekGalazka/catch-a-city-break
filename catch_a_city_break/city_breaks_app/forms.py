from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import TravelPlan


class CreateTravelPlanForm(ModelForm):
    class Meta:
        model = TravelPlan
        fields = ['name', 'description']

    def clean(self):
        cleaned_data = super().clean()
        plans = TravelPlan.objects.all()
        new_plan_name = cleaned_data['name']

        for plan in plans:
            if plan['name'] == new_plan_name:
                raise ValidationError('Such plan name already exist. Please choose another name for your plan.')

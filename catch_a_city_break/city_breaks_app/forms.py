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
        new_plan_name = cleaned_data['name']

        if new_plan_name == TravelPlan.objects.filter(name=new_plan_name):
            raise ValidationError('Such plan name already exist. Please choose another name for your plan.')


class ActivitySelectForm(forms.Form):
    WARSAW = 'WAR'
    KRAKOW = 'KRK'
    GDANSK = 'GDA'
    CITIES = [
        (WARSAW, 'Warsaw'),
        (KRAKOW, 'Krakow'),
        (GDANSK, 'Gdansk'),
    ]
    CLASSIC = 'CLS'
    CRAZY = 'CRZ'
    TYPE = [
        (CLASSIC, 'Classic'),
        (CRAZY, 'Crazy')
    ]
    activity_type = forms.ChoiceField(widget=forms.Select, choices=TYPE)
    city = forms.ChoiceField(widget=forms.Select, choices=CITIES)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     chosen_city = cleaned_data['city']
    #     chosen_activity_type = cleaned_data['activity_type']
    #
    #     if new_plan_name == TravelPlan.objects.filter(name=new_plan_name):
    #         raise ValidationError('Such plan name already exist. Please choose another name for your plan.')
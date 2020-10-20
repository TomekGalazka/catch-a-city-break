from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import TravelPlan, Activities


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
    activity_type = forms.ChoiceField(widget=forms.Select, choices=TYPE, initial='CLS')
    city = forms.ChoiceField(widget=forms.Select, choices=CITIES, initial='WAW')


class AddActivityToPlan(forms.Form):
    MONDAY = 'MON'
    TUESDAY = 'TUE'
    WEDNESDAY = 'WED'
    THURSDAY = 'THU'
    FRIDAY = 'FRI'
    SATURDAY = 'SAT'
    SUNDAY = 'SUN'
    DAYS = [
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]
    HOURS = [
        (1, '1:00 AM'),
        (2, '2:00 AM'),
        (3, '3:00 AM'),
        (4, '4:00 AM'),
        (5, '5:00 AM'),
        (6, '6:00 AM'),
        (7, '7:00 AM'),
        (8, '8:00 AM'),
        (9, '9:00 AM'),
        (10, '10:00 AM'),
        (11, '11:00 AM'),
        (12, '12:00 PM'),
        (13, '1:00 PM'),
        (14, '2:00 PM'),
        (15, '3:00 PM'),
        (16, '4:00 PM'),
        (17, '5:00 PM'),
        (18, '6:00 PM'),
        (19, '7:00 PM'),
        (20, '8:00 PM'),
        (21, '9:00 PM'),
        (22, '10:00 PM'),
        (23, '11:00 PM'),
        (24, '12:00 AM')
    ]
    travel_plan = forms.ModelChoiceField(queryset=TravelPlan.objects.all(), initial='')
    week_day = forms.ChoiceField(widget=forms.Select, choices=DAYS, initial='MON')
    time = forms.ChoiceField(widget=forms.Select, choices=HOURS, initial='8')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields['travel_plan'].queryset = TravelPlan.objects.filter(user=self.user)


    # travel_plan = models.ForeignKey(TravelPlan, on_delete=models.CASCADE)
    # activities = models.ForeignKey(Activities, on_delete=models.CASCADE)
    # # order = models.IntegerField()
    # week_day = models.ForeignKey(WeekDay, on_delete=models.CASCADE)
    # time = models.IntegerField(choices=HOURS)
    # user = models.ManyToManyField(User)
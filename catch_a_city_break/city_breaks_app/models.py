from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Activities(models.Model):
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
    name = models.CharField(max_length=256)
    description = models.TextField()
    duration = models.IntegerField()
    city = models.CharField(max_length=3, choices=CITIES)
    activity_type = models.CharField(max_length=3, choices=TYPE)
    image = models.ImageField()

    def __str__(self):
        return self.name


class TravelPlan (models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    activities = models.ManyToManyField(Activities, through='TravelPlanActivities')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WeekDay(models.Model):
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
    name = models.CharField(max_length=3, choices=DAYS)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return self.name


class TravelPlanActivities(models.Model):
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
    travel_plan = models.ForeignKey(TravelPlan, on_delete=models.CASCADE)
    activities = models.ForeignKey(Activities, on_delete=models.CASCADE)
    # order = models.IntegerField()
    week_day = models.ForeignKey(WeekDay, on_delete=models.CASCADE)
    time = models.IntegerField(choices=HOURS)
    user = models.ManyToManyField(User)


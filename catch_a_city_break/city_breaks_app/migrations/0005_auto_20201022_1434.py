# Generated by Django 2.2.16 on 2020-10-22 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('city_breaks_app', '0004_auto_20201018_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelplanactivities',
            name='activities',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='city_breaks_app.Activities'),
        ),
        migrations.AlterField(
            model_name='travelplanactivities',
            name='travel_plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='city_breaks_app.TravelPlan'),
        ),
    ]

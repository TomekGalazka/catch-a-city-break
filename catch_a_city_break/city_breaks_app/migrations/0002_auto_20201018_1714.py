# Generated by Django 2.2.16 on 2020-10-18 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_breaks_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelplanactivities',
            name='time',
            field=models.IntegerField(choices=[(1, '1:00 AM'), (2, '2:00 AM'), (3, '3:00 AM'), (4, '4:00 AM'), (5, '5:00 AM'), (6, '6:00 AM'), (7, '7:00 AM'), (8, '8:00 AM'), (9, '9:00 AM'), (10, '10:00 AM'), (11, '11:00 AM'), (12, '12:00 PM'), (13, '1:00 PM'), (14, '2:00 PM'), (15, '3:00 PM'), (16, '4:00 PM'), (17, '5:00 PM'), (18, '6:00 PM'), (19, '7:00 PM'), (20, '8:00 PM'), (21, '9:00 PM'), (22, '10:00 PM'), (23, '11:00 PM'), (24, '12:00 AM')]),
        ),
    ]

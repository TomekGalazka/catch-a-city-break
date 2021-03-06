# Generated by Django 2.2.16 on 2020-10-18 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('city_breaks_app', '0002_auto_20201018_1714'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='travelplan',
            constraint=models.UniqueConstraint(fields=('name', 'user'), name='A User can only have one Travel Plan with a same name'),
        ),
    ]

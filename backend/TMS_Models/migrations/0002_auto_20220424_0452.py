# Generated by Django 3.2.9 on 2022-04-24 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TMS_Models', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='HotelCountryId',
        ),
        migrations.RemoveField(
            model_name='hotels',
            name='HotelStateId',
        ),
    ]

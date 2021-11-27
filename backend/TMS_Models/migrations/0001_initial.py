# Generated by Django 3.2.8 on 2021-10-24 13:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts_Type',
            fields=[
                ('account_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('account_type_name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=255, null=True)),
                ('lname', models.CharField(max_length=255, null=True)),
                ('gender', models.CharField(max_length=50, null=True)),
                ('DOB', models.DateField(null=True)),
                ('Address', models.CharField(max_length=511, null=True)),
                ('Picture', models.CharField(max_length=255, null=True)),
                ('account_type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.accounts_type')),
            ],
        ),
        migrations.CreateModel(
            name='User_Auth',
            fields=[
                ('user_auth_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, null=True, unique=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('joinnig_date', models.DateField(default=datetime.date(2021, 10, 24))),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TMS_Models.users')),
            ],
        ),
    ]
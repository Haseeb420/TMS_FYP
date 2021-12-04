from django.db import models
from django.db.models.fields import DateField
from datetime import date

from django.db.models.fields.related import ForeignKey
# Create your models here.


class Accounts_Type(models.Model):
    account_type_id=models.AutoField(primary_key=True)
    account_type_name=models.CharField(max_length=255,null=True)

class Users(models.Model):
    user_id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=255,null=True)
    lname=models.CharField(max_length=255,null=True)
    gender=models.CharField(max_length=50,null=True)
    DOB=models.DateField(null=True)
    Address=models.CharField(max_length=511,null=True)
    Picture=models.CharField(max_length=255,null=True)
    account_type_id=models.ForeignKey(Accounts_Type,on_delete=models.CASCADE,null=True)

class User_Auth(models.Model):
    user_auth_id=models.AutoField(primary_key=True)
    email=models.EmailField(max_length=255,null=True,unique=True)
    password=models.CharField(max_length=255,null=True)
    joinnig_date=DateField(null=True)
    user_id=ForeignKey(Users,on_delete=models.CASCADE)


from django.db import models
from django.db.models.fields import DateField
from datetime import date

from django.db.models.fields.related import ForeignKey
# Create your models here.


class AccountsType(models.Model):
    AccountTypeId=models.AutoField(primary_key=True)
    AccountTypeName=models.CharField(max_length=255,null=True)

class Users(models.Model):
    UserId=models.AutoField(primary_key=True)
    Fname=models.CharField(max_length=255,null=True)
    Lname=models.CharField(max_length=255,null=True)
    Gender=models.CharField(max_length=50,null=True)
    UserDOB=models.DateField(null=True)
    Address=models.CharField(max_length=511,null=True)
    Picture=models.CharField(max_length=255,null=True)
    AccountTypeId=models.ForeignKey(Accounts_Type,on_delete=models.CASCADE,null=True)

class UserAuth(models.Model):
    UserAuthId=models.AutoField(primary_key=True)
    Email=models.EmailField(max_length=255,null=True,unique=True)
    Password=models.CharField(max_length=255,null=True)
    JoinnigDate=DateField(null=True)
    UserId=ForeignKey(Users,on_delete=models.CASCADE)
    
    
class PackageTypes(models.Model):
    PackageTypeId=models.AutoField(primary_key=True)
    PackageTypeName=models.CharField(max_length=255,null=True)
     
class Packages(models.Model):
    PackageId=models.AutoField(primary_key=True)
    PackagePrice=models.IntegerField(null=True)
    PackageisActive=models.BooleanField(default=True)
    PackageDescription=models.CharField(max_length=511,null=True)
    PackageTypeId=models.ForeignKey(Package_Types,on_delete=models.CASCADE,null=True)

    
class PackageImages(models.Model):
    PackageImageId=models.AutoField(primary_key=True)
    PackageImageURL=models.CharField(max_length=255,null=True)
    PackageId=models.ForeignKey(Packages,on_delete=models.CASCADE,null=True)
    

class HotelType(models.Model):
    HotelTypeId=models.AutoField(primary_key=True)
    HotelTypeName=models.CharField(max_length=255,null=True)
    
    
class HotelsOwner(models.Model):
    HotelOwnerId=models.AutoField(primary_key=True)
    HotelOwnerName=models.CharField(max_length=255,null=True)
    HotelOwnerPhone=models.CharField(max_length=255,null=True)

class Hotel(models.Model):
    HotelId=models.AutoField(primary_key=True)
    HotelName=models.CharField(max_length=255,null=True)
    HotelAddress=models.CharField(max_length=511,null=True)
    HotelDescription=models.CharField(max_length=511,null=True)
    HotelTypeId=models.ForeignKey(Hotel_Type,on_delete=models.CASCADE,null=True)
    HotelOwnerId=models.ForeignKey(Hotels_Owner,on_delete=models.CASCADE,null=True)
    
class VehicleOwner(models.Model):
    VehicleOwnerId=models.AutoField(primary_key=True)
    VehicleOwnerName=models.CharField(max_length=255,null=True)
    VehicleOwnerPhone=models.CharField(max_length=255,null=True)
    
class VehicleType(models.Model):
    VehicleTypeId=models.AutoField(primary_key=True)
    VehicleTypeName=models.CharField(max_length=255,null=True)
    
    
class Vehicles(models.Model):
    VehicleId=models.AutoField(primary_key=True)
    VehicleModel=models.CharField(max_length=255,null=True)
    VehicleNumber=models.CharField(max_length=255,null=True)
    VehicleOwnerId=models.ForeignKey(Vehicle_Owner,on_delete=models.CASCADE,null=True)
    VehicleTypeId=models.ForeignKey(Vehicle_Type,on_delete=models.CASCADE,null=True)
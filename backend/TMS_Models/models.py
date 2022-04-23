from distutils.command.upload import upload
from django.db import models
from django.db.models.fields import DateField
from datetime import date

from django.db.models.fields.related import ForeignKey
# Create your models here.

"""
Users related models starts here
"""


class AccountsType(models.Model):
    AccountsTypeId = models.AutoField(primary_key=True)
    AccountTypeName = models.CharField(max_length=255, null=True)


class Users(models.Model):
    UserId = models.AutoField(primary_key=True)
    Fname = models.CharField(max_length=255, null=True)
    Lname = models.CharField(max_length=255, null=True)
    Gender = models.CharField(max_length=50, null=True)
    UserDOB = models.DateField(null=True)
    Address = models.CharField(max_length=511, null=True)
    Picture = models.ImageField(upload_to="users_profile")
    AccountTypeId = models.ForeignKey(
        AccountsType, on_delete=models.CASCADE, null=True)


class UserAuth(models.Model):
    UserAuthId = models.AutoField(primary_key=True)
    Email = models.EmailField(max_length=255, null=True, unique=True)
    Password = models.CharField(max_length=255, null=True)
    JoinnigDate = DateField(null=True)
    user_saltkey = models.CharField(max_length=255, null=True)
    UserId = ForeignKey(Users, on_delete=models.CASCADE)


"""
Users related models ends here
"""

"""
State, city, country related models starts here
"""


class Country(models.Model):
    CountryId = models.AutoField(primary_key=True)
    CountryName = models.CharField(max_length=255, null=True)


class State(models.Model):
    StateId = models.AutoField(primary_key=True)
    StateName = models.CharField(max_length=255, null=True)
    CountryId = ForeignKey(Country, on_delete=models.CASCADE)


class City(models.Model):
    CityId = models.AutoField(primary_key=True)
    CityName = models.CharField(max_length=255, null=True)
    StateId = ForeignKey(State, on_delete=models.CASCADE)


""" 
State, city, country related models ends here
"""

"""
Hotels and Rooms related models starts here
"""


class HotelsType(models.Model):
    HotelsTypeId = models.AutoField(primary_key=True)
    HotelsTypeName = models.CharField(max_length=255, null=True)


class Hotels(models.Model):
    HotelId = models.AutoField(primary_key=True)
    HotelName = models.CharField(max_length=255, null=True)
    HotelAddress = models.CharField(max_length=511, null=True)
    HotelCityId = ForeignKey(City, on_delete=models.CASCADE)
    HotelContact = models.CharField(max_length=255, null=True)
    HotelEmail = models.EmailField(max_length=255, null=True)
    HotelTypeId = ForeignKey(HotelsType, on_delete=models.CASCADE)
    HotelPicture = models.ImageField(upload_to="hotels_profile")


class Rooms(models.Model):
    RoomId = models.AutoField(primary_key=True)
    RoomName = models.CharField(max_length=255, null=True)
    RoomType = models.CharField(max_length=255, null=True)
    RoomPrice = models.IntegerField(null=True)
    RoomDescription = models.CharField(max_length=511, null=True)
    RoomPicture = models.ImageField(upload_to="rooms_profile")
    HotelId = ForeignKey(Hotels, on_delete=models.CASCADE)


class HotelBill(models.Model):
    HotelBillId = models.AutoField(primary_key=True)
    HotelBillDate = DateField(null=True)
    HotelBillAmount = models.IntegerField(null=True)
    HotelBillStatus = models.CharField(max_length=255, null=True)
    HotelId = ForeignKey(Hotels, on_delete=models.CASCADE)


class HotelOwner(models.Model):
    HotelOwnerId = models.AutoField(primary_key=True)
    HotelOwnerName = models.CharField(max_length=255, null=True)
    HotelOwnerContact = models.CharField(max_length=255, null=True)
    HotelOwnerEmail = models.EmailField(max_length=255, null=True)
    HotelOwnerAddress = models.CharField(max_length=511, null=True)
    HotelId = ForeignKey(Hotels, on_delete=models.CASCADE)


"""
Hotels and Rooms related models ends here
"""

"""
vehicles related models starts here

"""


class VehicleType(models.Model):
    VehicleTypeId = models.AutoField(primary_key=True)
    VehicleTypeName = models.CharField(max_length=255, null=True)


class Vehicles(models.Model):
    VehicleId = models.AutoField(primary_key=True)
    VehicleName = models.CharField(max_length=255, null=True)
    VehicleTypeId = ForeignKey(VehicleType, on_delete=models.CASCADE)
    VehiclePrice = models.IntegerField(null=True)
    VehicleDescription = models.CharField(max_length=511, null=True)
    VehiclePicture = models.ImageField(upload_to="vehicles_profile")


class VehicleBill(models.Model):
    VehicleBillId = models.AutoField(primary_key=True)
    VehicleBillDate = DateField(null=True)
    VehicleBillAmount = models.IntegerField(null=True)
    VehicleBillStatus = models.CharField(max_length=255, null=True)
    VehicleId = ForeignKey(Vehicles, on_delete=models.CASCADE)


"""
vehicles related models ends here

"""

"""
Packages related models starts here
"""


class PackagesType(models.Model):
    PackagesTypeId = models.AutoField(primary_key=True)
    PackagesTypeName = models.CharField(max_length=255, unique=True)


class Packages(models.Model):
    PackageId = models.AutoField(primary_key=True)
    PackageName = models.CharField(max_length=255, unique=True)
    PackageTypeId = ForeignKey(PackagesType, on_delete=models.CASCADE)
    PackagePrice = models.IntegerField(null=True)
    PackageDescription = models.CharField(max_length=511, null=True)
    PackagePicture = models.ImageField(upload_to="packages_profile")
    HotelId = ForeignKey(Hotels, on_delete=models.CASCADE)
    vehicleId = ForeignKey(Vehicles, on_delete=models.CASCADE, null=True)


"""
Packages related models ends here
"""

""" 
Booking , invoice, sales, transactions, profitRatio related models starts here
"""


class Booking(models.Model):
    BookingId = models.AutoField(primary_key=True)
    BookingDate = DateField(null=True)
    BookingAmount = models.IntegerField(null=True)
    BookingStatus = models.CharField(max_length=255, null=True)
    BookingUserId = ForeignKey(Users, on_delete=models.CASCADE)
    BookingPackageId = ForeignKey(
        Packages, on_delete=models.CASCADE, null=True)


class Payment(models.Model):
    PaymentId = models.AutoField(primary_key=True)
    PaymentDate = DateField(null=True)
    PaymentAmount = models.IntegerField(null=True)
    # PaymentStatus = models.CharField(max_length=255, null=True) make it true after payment
    PaymentStatus = models.BooleanField(default=False)
    PaymentUserId = ForeignKey(Users, on_delete=models.CASCADE)
    PaymentBookingId = ForeignKey(Booking, on_delete=models.CASCADE)


class Invoice(models.Model):
    InvoiceId = models.AutoField(primary_key=True)
    InvoiceDate = DateField(null=True)
    InvoiceAmount = models.IntegerField(null=True)
    InvoiceStatus = models.CharField(max_length=255, null=True)
    InvoiceUserId = ForeignKey(Users, on_delete=models.CASCADE)
    InvoiceBookingId = ForeignKey(Booking, on_delete=models.CASCADE)


class SalesReport(models.Model):
    salesId = models.AutoField(primary_key=True)
    salesDate = DateField(null=True)
    salesAmount = models.IntegerField(null=True)
    salesStatus = models.CharField(max_length=255, null=True)
    salesUserId = ForeignKey(Users, on_delete=models.CASCADE)
    salesBookingId = ForeignKey(Booking, on_delete=models.CASCADE)

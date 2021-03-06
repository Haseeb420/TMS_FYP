from asyncore import read
from dataclasses import field
from rest_framework import serializers
from TMS_Models import models

"""
User related serializers starts here
"""


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserAuth
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    credentials = UserAuthSerializer(many=True, read_only=True)

    class Meta:
        model = models.Users
        fields = '__all__'


class AccountsTypeSerializer(serializers.ModelSerializer):
    user_type = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = models.AccountsType
        fields = '__all__'


"""
User related serializers ends here
"""


"""
Package related serializers starts here
"""


class PackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Packages
        fields = '__all__'


class PackagesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PackagesType
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = models.State
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True, read_only=True)

    class Meta:
        model = models.Country
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hotels
        fields = '__all__'


class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rooms
        fields = '__all__'


class HotelsTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelsType
        fields = '__all__'


class HotelBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelBill
        fields = '__all__'


class HotelOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotelOwner
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VehicleType
        fields = '__all__'


class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vehicles
        fields = '__all__'


class VehicleBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VehicleBill
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Payment
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Invoice
        fields = '__all__'


class SalesReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SalesReport
        fields = '__all__'


class ManageSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SliderModel
        fields = '__all__'

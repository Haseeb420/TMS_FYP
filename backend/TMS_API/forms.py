from cProfile import label
from dataclasses import fields
from tkinter import Widget
from django import forms
from TMS_Models import models


class VehiclesForm(forms.ModelForm):
    class Meta:
        model = models.Vehicles
        fields = ["VehicleName", "VehicleTypeId",
                  "VehiclePrice", "VehicleDescription", "VehiclePicture", "Is_available"]
        labels = {
            "VehicleName": "Vehicle Name",
            "VehicleTypeId": "Vehicle Type",
            "VehiclePrice": "Vehicle Price",
            "VehicleDescription": "Vehicle Description",
            "VehiclePicture": "Vehicle Picture",
            "Is_available": "Vehicle Status"
        }
        widgets = {
            "VehicleName": forms.TextInput(attrs={"classs": "form-control"}),
            "VehicleTypeId": forms.Select(attrs={"classs": "form-control"}),
            "VehiclePrice": forms.NumberInput(attrs={"classs": "form-control"}),
            "VehicleDescription": forms.Textarea(attrs={"classs": "form-control"}),
            "VehiclePicture": forms.FileInput(attrs={"classs": "form-control"}),
            "Is_available": forms.CheckboxInput(attrs={"classs": "form-control"}),
        }
        error_messages = {
            "VehicleName": {
                "required": "Vehicle Name is required",
                "max_length": "Vehicle Name is too long",
            },
            "VehicleTypeId": {
                "required": "Vehicle Type is required",
                "max_length": "Vehicle Type is too long",
            },
            "VehiclePrice": {
                "required": "Vehicle Price is required",
                "max_length": "Vehicle Price is too long",
            },
            "VehicleDescription": {
                "required": "Vehicle Description is required",
                "max_length": "Vehicle Description is too long",
            },
            "VehiclePicture": {
                "required": "Vehicle Picture is required",
                "max_length": "Vehicle Picture is too long",
            },
            "Is_available": {
                "required": "Vehicle Status is required",
                "max_length": "Vehicle Status is too long",
            },
        }

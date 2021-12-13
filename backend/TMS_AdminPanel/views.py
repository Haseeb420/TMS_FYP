from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
# Create your views here.

_SiteName = "-Royal Travels"


class IndexView(View):
    _template_name = "AdminSide/templates/dashboard.html"
    _title = "Dashboard"+_SiteName

    def get(self, request):
        data = {"title": self._title}
        return render(request, self._template_name, data)


""""
     All Packages views are start from here
"""

"""
Packages List view code start from here

"""


class PackageView(View):
    template_name = "AdminSide/templates/Packages/Packages.html"
    _title = "Packages"+_SiteName

    def get(self, request):
        data = {"title": self._title}
        return render(request, self.template_name, data)


"""
Packages List view code End from here

"""

"""
Packages List view code start from here

"""


class AddPackage(View):
    template_name = "AdminSide/templates/Packages/AddPackages.html"
    _title = "AddPackages"+_SiteName

    def get(self, request):
        data = {"title": self._title}
        return render(request, self.template_name, data)


"""
Packages List view code End from here

"""


""""
     All Packages views are ends here 
"""


"""
All users views code start here
"""


"""User List view code starts here"""


class ManageUsers(View):
    template_name = "AdminSide/templates/Users/users.html"
    _title = "Users"+_SiteName

    def get(self, request):
        data = {"title": self._title}
        return render(request, self.template_name, data)


"""User List view code ends here"""


"""
All users views code ends here
"""


class ProductView(View):
    template_name = "AdminSide/templates/product_list.html"

    def get(self, request):
        return render(request, self.template_name)


class AddProductView(View):
    template_name = "AdminSide/templates/add_product.html"

    def get(self, request):
        return render(request, self.template_name)


class EditProductView(View):
    template_name = "AdminSide/templates/edit_product.html"

    def get(self, request):
        return render(request, self.template_name)


class DashboardView(View):
    template_name = "AdminSide/templates/dashboard.html"

    def get(self, request):
        return render(request, self.template_name)




class Add_VehicleOwnerView(View):
    template_name = "AdminSide/templates/Vehicle_Owners/add_vehicleOwner.html"
class AddVehicles(View):
    template_name = "AdminSide/templates/Vehicles/add_vehicle.html"

    def get(self, request):
        return render(request, self.template_name)

class Edit_VehicleOwnerView(View):
    template_name = "AdminSide/templates/Vehicle_Owners/edit_vehicleOwner.html"
class EditVehicles(View):
    template_name = "AdminSide/templates/Vehicles/edit_vehicle.html"

    def get(self, request):
        return render(request, self.template_name)

class Show_VehicleOwnerView(View):
    template_name = "AdminSide/templates/Vehicle_Owners/list_vehicleOwner.html"
class ViewVehicles(View):
    template_name = "AdminSide/templates/Vehicles/vehicle_list.html"

    def get(self, request):
        return render(request, self.template_name)


        
class Add_HotelView(View):
    template_name = "AdminSide/templates/Hotels/add_hotel.html"
class CategoryView(View):
    template_name = "AdminSide/templates/Category/category.html"
class ManageTransactions(View):
    template_name = "AdminSide/templates/sales-transaction/transactions.html"

    def get(self, request):
        return render(request, self.template_name)

class Edit_HotelView(View):
    template_name = "AdminSide/templates/Hotels/edit_hotel.html"
class ProfileView(View):
    template_name = "AdminSide/templates/profile.html"
class ManageSales(View):
    template_name = "AdminSide/templates/sales-transaction/sales.html"

    def get(self, request):
        return render(request, self.template_name)

class Show_HotelView(View):
    template_name = "AdminSide/templates/Hotels/list_hotels.html"

    def get(self, request):
        return render(request, self.template_name)
class ChangePassword(View):
    template_name = "AdminSide/templates/change-password.html"

    def get(self, request):
        return render(request, self.template_name)

class ManageFeedback(View):
    template_name = "AdminSide/templates/sales-transaction/feedback.html"

    def get(self, request):
        return render(request, self.template_name)

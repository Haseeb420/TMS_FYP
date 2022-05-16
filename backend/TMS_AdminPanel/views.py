from django.shortcuts import render

from django.views.generic import TemplateView
# Create your views here.

_SiteName = "-Royal Travels"
_404Page = "AdminSide/templates/shared/404.html"


class DashboardView(TemplateView):
    template_name = 'AdminSide/templates/AdminUI/index.html'

    def get(self, request):
        try:
            return render(request, self.template_name, {'siteName': "Dashboard"+_SiteName})
        except:
            return render(request, _404Page, {'siteName': "Dashboard"+_SiteName})


class AccountsTypeView(TemplateView):
    template_name = 'AdminSide/templates/Accounts/AccountsType.html'

    def get(self, request):
        return render(request, self.template_name, {'siteName': "Accounts Type"+_SiteName})


class AddAccountsTypeView(TemplateView):
    template_name = 'AdminSide/templates/Accounts/AddAccountsType.html'

    def get(self, request):
        return render(request, self.template_name, {'siteName': "Accounts Type"+_SiteName})


"""
All users views code start here
"""


"""User List view code starts here"""


class ManageUsers(TemplateView):
    template_name = "AdminSide/templates/Users/Users.html"
    _title = "Users"+_SiteName

    def get(self, request):
        return render(request, self.template_name, {'siteName': self._title})


"""User List view code ends here"""


"""
All users views code ends here
"""


class VehicleTypeView(TemplateView):
    template_name = 'AdminSide/templates/Vehicles/vehiclesTypes.html'
    _title = "Vehicle Type"+_SiteName

    def get(self, request):
        return render(request, self.template_name, {'siteName': self._title})


class ViewVehicles(TemplateView):
    template_name = "AdminSide/templates/Vehicles/vehicles.html"
    _title = "Vehicles"+_SiteName

    def get(self, request):
        return render(request, self.template_name, {'siteName': self._title})

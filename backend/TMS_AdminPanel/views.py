
from django.urls import reverse
from django.shortcuts import render
from TMS_AdminPanel.forms import LoginForm
from django.views.generic import TemplateView, View
from TMS_Models import models
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

_SiteName = "-Royal Travels"
_404Page = "AdminSide/templates/shared/404.html"


class LoginView(View):
    template_name = "AdminSide/templates/shared/admin_login.html"
    _title = "Login"+_SiteName

    def get(self, request, *args, **kwargs):
        login_form = LoginForm()
        return render(request, self.template_name, {"siteName": self._title, "login_form": login_form, 'error': kwargs.get('error')})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            try:
                user_auth = models.UserAuth.objects.get(
                    Email=email, Password=password)
                print(user_auth.UserId.Fname)
                if user_auth.UserId.AccountsTypeId.AccountsTypeId == 1:
                    request.session['user_id'] = user_auth.UserId.UserId
                    request.session['user_name'] = user_auth.UserId.Fname
                    request.session['account_type_id'] = user_auth.UserId.AccountsTypeId.AccountsTypeId
                    rendered_url = reverse('TMS_AdminPanel:dashboard')
                    return HttpResponseRedirect(rendered_url)

                else:
                    return render(request, "AdminSide/templates/shared/admin_login.html", {"login_form": login_form, "error": "You dont have permission to access this page"})
            except models.UserAuth.DoesNotExist:
                return render(request, "AdminSide/templates/shared/admin_login.html", {"login_form": login_form, "error": "Invalid Credentials"})
        else:
            return render(request, self.template_name, {"siteName": self._title, "login_form": login_form})


class DashboardView(TemplateView):
    template_name = 'AdminSide/templates/AdminUI/index.html'
    _title = "Dashboard"+_SiteName

    def get(self, request):
        if 'user_id' in request.session and request.session['account_type_id'] == 1:

            return render(request, self.template_name, {"siteName": self._title})
        else:
            return HttpResponseRedirect(reverse('TMS_AdminPanel:index'))


class AccountsTypeView(TemplateView):
    template_name = 'AdminSide/templates/Accounts/AccountsType.html'

    def get(self, request):

        if 'user_id' in request.session and request.session['account_type_id'] == 1:
            return render(request, self.template_name, {'siteName': "Accounts Type"+_SiteName})
        else:
            return HttpResponseRedirect(reverse('TMS_AdminPanel:index'))


class AddAccountsTypeView(TemplateView):
    template_name = 'AdminSide/templates/Accounts/AddAccountsType.html'

    def get(self, request):
        if 'user_id' in request.session and request.session['account_type_id'] == 1:
            return render(request, self.template_name, {'siteName': self._title})
        else:
            return HttpResponseRedirect(reverse('TMS_AdminPanel:index'))


"""
All users views code start here
"""


"""User List view code starts here"""


class ManageUsers(TemplateView):
    template_name = "AdminSide/templates/Users/Users.html"
    _title = "Users"+_SiteName

    def get(self, request):
        if 'user_id' in request.session and request.session['account_type_id'] == 1:
            return render(request, self.template_name, {'siteName': self._title})
        else:
            return HttpResponseRedirect(reverse('TMS_AdminPanel:index'))


"""User List view code ends here"""


"""
All users views code ends here
"""


class VehicleTypeView(TemplateView):
    template_name = 'AdminSide/templates/Vehicles/vehiclesTypes.html'
    _title = "Vehicle Type"+_SiteName

    def get(self, request):
        if 'user_id' in request.session and request.session['account_type_id'] == 1:
            return render(request, self.template_name, {'siteName': self._title})

        else:
            return HttpResponseRedirect(reverse('TMS_AdminPanel:index'))


class ViewVehicles(TemplateView):
    template_name = "AdminSide/templates/Vehicles/vehicles.html"
    _title = "Vehicles"+_SiteName

    def get(self, request):
        if 'user_id' in request.session and request.session['account_type_id'] == 1:
            return render(request, self.template_name, {'siteName': self._title})
        else:
            return HttpResponseRedirect(reverse('TMS_AdminPanel:index'))


class HotelsView(TemplateView):
    template_name = "AdminSide/templates/Hotels/hotels.html"
    _title = "Hotels List"+_SiteName

    def get(self, request):
        if 'user_id' in request.session and request.session['account_type_id'] == 1:
            return render(request, self.template_name, {'siteName': self._title})
        else:
            return HttpResponseRedirect(reverse('TMS_AdminPanel:index'))


class HotelTypeView(TemplateView):
    template_name = "AdminSide/templates/Hotels/hotels_types.html"
    _title = "Hotels Type"+_SiteName

    def get(self, request):
        if 'user_id' in request.session and request.session['account_type_id'] == 1:
            return render(request, self.template_name, {'siteName': self._title})
        else:
            return HttpResponseRedirect(reverse('TMS_AdminPanel:index'))


class CounteriesView(View):
    template_name = "AdminSide/templates/Regions/countries.html"
    _title = "Countries"+_SiteName

    def get(self, request):
        if 'user_id' in request.session and request.session['account_type_id'] == 1:
            return render(request, self.template_name, {'siteName': self._title})
        else:
            return HttpResponseRedirect(reverse('TMS_AdminPanel:index'))


class StatesView(View):
    template_name = "AdminSide/templates/Regions/states.html"
    _title = "States"+_SiteName

    def get(self, request):
        if 'user_id' in request.session and request.session['account_type_id'] == 1:
            return render(request, self.template_name, {'siteName': self._title})
        else:
            return HttpResponseRedirect(reverse('TMS_AdminPanel:index'))


class CityView(View):
    template_name = "AdminSide/templates/Regions/cities.html"
    _title = "Cities"+_SiteName

    def get(self, request):
        if 'user_id' in request.session and request.session['account_type_id'] == 1:
            return render(request, self.template_name, {'siteName': self._title})
        else:
            return HttpResponseRedirect(reverse('TMS_AdminPanel:index'))

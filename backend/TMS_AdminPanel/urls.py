
from django.urls import path
from .views import *


app_name = 'TMS_AdminPanel'
urlpatterns = [
    # path("",TemplateView.as_view(template_name='AdminSide/index.html')),
    path("", LoginView.as_view(), name="index"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    # users views url start here
    path("manage-users", ManageUsers.as_view(), name="manage-users"),
    path("manage_accounts_Types", AccountsTypeView.as_view(),
         name="manage_accounts_Types"),
    path("add_accounts_Types", AddAccountsTypeView.as_view(),
         name="add_accounts_Types"),
    # users views url end here

    # vehicles views urls starts from here
    path("vehicle-type", VehicleTypeView.as_view(), name="vehicle-type"),
    path("list-vehicles", ViewVehicles.as_view(), name="list-vehicles"),

    # vehicles views urls code ends here

    # hotels views urls code starts here
    path("hotels-list", HotelsView.as_view(), name="hotels-list"),
    path("hotels-types", HotelTypeView.as_view(), name="hotels-types"),
    # hotels views urls code ends here

    # regions related urls start here
    path("countries", CounteriesView.as_view(), name="countries"),
    path("states", StatesView.as_view(), name="states"),
    path("cities", CityView.as_view(), name="cities"),

    # regions related urls ends here

    # packages related urls starts here
    path("packages-list", PackagesView.as_view(), name="packages-list"),
    path("packages-type", PackagesTypeView.as_view(), name="packages-type"),
    # packages related urls ends here

]

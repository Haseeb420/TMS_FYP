
from django.urls import path
from .views import *


app_name = 'TMS_AdminPanel'
urlpatterns = [
    # path("",TemplateView.as_view(template_name='AdminSide/index.html')),
    path("", DashboardView.as_view(), name="index"),
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

    # vehicles views urls code end here








]

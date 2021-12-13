from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'TMS_AdminPanel'
urlpatterns = [
    # path("",TemplateView.as_view(template_name='AdminSide/index.html')),
    path("", IndexView.as_view(), name="index"),


    # packages views urls starts from here

    path("manage-packages", PackageView.as_view(), name="manage-packages"),
    path("add-packages", AddPackage.as_view(), name="add-packages"),

    # packages views urls code end here


    # vehicles views urls starts from here
    path("add-vehicles", AddVehicles.as_view(), name="add-vehicles"),
    path("edit-vehicles", EditVehicles.as_view(), name="edit-vehicles"),
    path("list-vehicles", ViewVehicles.as_view(), name="list-vehicles"),

    # vehicles views urls code end here

    # category url starts here
    path('categories', CategoryView.as_view(), name="categories"),
    # category url ends here




    # users views url start here
    path("manage-users", ManageUsers.as_view(), name="manage-users"),
    # users views url end here


    # sales and transactions views url start here
    path("manage-transactions", ManageTransactions.as_view(),
         name="manage-transactions"),

    path("manage-sales", ManageSales.as_view(), name="manage-sales"),
    # sales and transactions views url end here

    path("manage-feedback", ManageFeedback.as_view(), name="manage-feedback"),




    path("manage-products", ProductView.as_view(), name="manage-products"),
    path("add-products", AddProductView.as_view(), name="add-products"),
    path("edit-products", EditProductView.as_view(), name="edit-products"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),

    path("add_VehicleOwner", Add_VehicleOwnerView.as_view(),
         name="add_VehicleOwner"),
    path("edit_VehicleOwner", Edit_VehicleOwnerView.as_view(),
         name="edit_VehicleOwner"),
    path("show_VehicleOwner", Show_VehicleOwnerView.as_view(),
         name="show_VehicleOwner"),

    path("add_hotel", Add_HotelView.as_view(), name="add_hotel"),
    path("edit_hotel", Edit_HotelView.as_view(), name="edit_hotel"),
    path("show_hotels", Show_HotelView.as_view(), name="show_hotels"),


    path("profile", ProfileView.as_view(), name="profile"),
    path("change_password", Change_passwordView.as_view(), name="change_password"),
    path("manage_ui", manage_uiView.as_view(), name="manage_ui"),
    path("add_image", add_imageView.as_view(), name="add_image"),
]

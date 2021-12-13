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

    # users views url start here
    path("manage-users", ManageUsers.as_view(), name="manage-users"),
    # users views url end here



    path("manage-products", ProductView.as_view(), name="manage-products"),
    path("add-products", AddProductView.as_view(), name="add-products"),
    path("edit-products", EditProductView.as_view(), name="edit-products"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("change_password", Change_passwordView.as_view(), name="change_password"),
    path("manage_ui", manage_uiView.as_view(), name="manage_ui"),
    path("add_image", add_imageView.as_view(), name="add_image"),
]

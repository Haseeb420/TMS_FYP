from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'TMS_AdminPanel'
urlpatterns = [
    # path("",TemplateView.as_view(template_name='AdminSide/index.html')),
    path("", IndexView.as_view(), name="index"),
    path("manage-packages", PackageView.as_view(), name="manage-packages"),
    path("manage-products", ProductView.as_view(), name="manage-products"),
    path("add-products", AddProductView.as_view(), name="add-products"),
    path("edit-products", EditProductView.as_view(), name="edit-products"),
    path("dashboard", DashboardView.as_view(), name="dashboard"),

]

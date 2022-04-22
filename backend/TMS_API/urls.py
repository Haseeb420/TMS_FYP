from django.urls import path, include
from TMS_API import views
from rest_framework import routers


r = routers.DefaultRouter()
r.register('accout_type_api', views.AccountsTypeView,
           basename='accout_type_api')
r.register('package_type_api', views.PackageTypeView,
           basename='package_type_api')

urlpatterns = [
    path("users_api/", views.UsersView.as_view()),
    path("users_api/<int:pk>/", views.UsersView.as_view()),
    path("", include(r.urls)),
    path("user_auth_api/", views.UserAuthView.as_view()),
    path("user_auth_api/<int:pk>/", views.UserAuthView.as_view()),


    # Packages api Urls starts here

    path("packages_api/", views.PackageView.as_view()),
    path("packages_api/<int:pk>/", views.PackageView.as_view()),

    # Packages api Urls ends here

]

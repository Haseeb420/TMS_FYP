from multiprocessing.dummy import Namespace
from django.urls import path, include
from TMS_API import views
from rest_framework import routers

r = routers.DefaultRouter()
r.register('country', views.CountryView, basename='country')
r.register('state', views.StateView, basename='state')
r.register('city', views.CityView, basename='city')
r.register('accout_type_api', views.AccountsTypeView,
           basename='accout_type_api')
r.register('package_type_api', views.PackageTypeView,
           basename='package_type_api')
r.register("hotel_type_api", views.HotelsTypeView, basename="hotel_type_api")
r.register("vehicle_type_api", views.VehicleTypeView,
           basename="vehicle_type_api")

urlpatterns = [
    path("", include(r.urls)),

    # ---------------------------------------------------------------------------------

    # users api urls start here

    path("users_api/", include([
        path("", views.UsersView.as_view()),
        path("<int:pk>/", views.UsersView.as_view()),
    ])),
    path("user_auth_api/", include([
        path("<int:pk>/", views.UserAuthView.as_view()),
        path("", views.UserAuthView.as_view()), ])),


    # users api urls end here

    # -----------------------------------------------------------------------

    # hotels api urls start here
    path("hotels_api/", include([
        path("", views.HotelsView.as_view()),
        path("<int:pk>/", views.HotelsView.as_view()),
    ])),

    # hotels api urls end here

    # -----------------------------------------------------------------------

    # vehicles api urls start here

    path("vehicles_api/", include([
        path("", views.VehicleView.as_view()),
        path("<int:pk>/", views.VehicleView.as_view()),
    ])),

    # vehicles api urls end here

    # -----------------------------------------------------------------------

    # Packages api Urls starts here
    path("packages_api/", include([
        path("", views.PackageView.as_view()),
        path("<int:pk>/", views.PackageView.as_view()),
    ])),
    # Packages api Urls ends here

]

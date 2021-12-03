from django.urls import path

from shop.views import *

urlpatterns = [
    path("allcities/",AllCities.as_view(), name="all-cities"),
    path("createcity/", CreateCity.as_view(), name="create-city")
]

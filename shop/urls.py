from django.urls import path

from shop.views import *

urlpatterns = [
    path("allcities/",AllCities.as_view(), name="all-cities"),
    path("allareazones/",AllCities.as_view(), name="all-areazones"),
    path("createcity/", CreateCity.as_view(), name="create-city"),
    path("createarea/", CreateAreaZone.as_view(), name="create-area"),
]

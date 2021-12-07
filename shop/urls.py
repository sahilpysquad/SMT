from django.urls import path

from .views import *

urlpatterns = [
    path("allcities/",AllCities.as_view(), name="all-cities"),
    path("allareazones/",AreaZoneListView.as_view(), name="all-areazones"),
    path("createcity/", CreateCity.as_view(), name="create-city"),
    path("createarea/", CreateAreaZone.as_view(), name="create-area"),
    path("updatecity/<int:pk>/", UpdateCity.as_view(), name="update-city"),
    path("updatearea/<int:pk>/", UpdateAreaZone.as_view(), name="update-area"),
    path("deletecity/<int:pk>/", DeleteCity.as_view(), name="delete-city"),
    path("deletearea/<int:pk>/", DeleteArea.as_view(), name="delete-area")
]

from django.views.generic import ListView, CreateView

from shop.forms import CreateCityForm
from shop.models import City, AreaZone


class AllCities(ListView):
    template_name = "shopemanagement/allcities.html"
    context_object_name = "cities"
    model = City


class CreateCity(CreateView):
    form_class = CreateCityForm
    template_name = "shopemanagement/createcity.html"
    success_url = "/shop/allcities/"


class CreateAreaZone(CreateView):
    model = AreaZone
    fields = ['name','city', 'pincode']
    success_url = "/shop/allareazones/"
    template_name = "shopemanagement/createareazone.html"


class AreaZoneListView(ListView):
    model = AreaZone
    template_name = "shopemanagement/allareazone.html"

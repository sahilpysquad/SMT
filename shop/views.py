from django.views.generic import ListView, CreateView

from shop.forms import CreateCityForm
from shop.models import City


class AllCities(ListView):
    template_name = "shopemanagement/allcities.html"
    context_object_name = "cities"
    model = City


class CreateCity(CreateView):
    form_class = CreateCityForm
    template_name = "shopemanagement/createcity.html"
    success_url = "/shoppermanagement/allcities/"

from django.views.generic import ListView, CreateView, UpdateView

from shop.forms import CreateCityForm
from shop.models import City, AreaZone, Shop


class AllCities(ListView):
    template_name = "shopemanagement/allcities.html"
    context_object_name = "cities"
    model = City


class CreateCity(CreateView):
    form_class = CreateCityForm
    template_name = "shopemanagement/createcity.html"
    success_url = "/shop/allcities/"


class UpdateCity(UpdateView):
    model = City
    template_name = "shopemanagement/createcity.html"
    fields = "__all__"
    success_url = "/shop/allcities/"


class CreateAreaZone(CreateView):
    model = AreaZone
    fields = ['name','city', 'pincode']
    success_url = "/shop/allareazones/"
    template_name = "shopemanagement/createareazone.html"


class AreaZoneListView(ListView):
    model = AreaZone
    template_name = "shopemanagement/allareazone.html"
    # paginate_by = 2
    
    def get_queryset(self):
        areazones = AreaZone.objects.all()
        search_city = self.request.GET.get("search_field")
        if search_city:
            city = City.objects.get(name=search_city)
            areazones = AreaZone.objects.filter(city=city)
            return areazones
        print(search_city)
        return areazones

class CreateShop(CreateView):
    model = Shop


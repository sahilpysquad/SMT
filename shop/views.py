from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import response
from shop.forms import CreateCityForm
from shop.models import City, AreaZone, Shop, SmtUsers



class AllCities(ListView):
    template_name = "shopemanagement/allcities.html"
    context_object_name = "cities"
    model = City


class CreateCity(CreateView):
    form_class = CreateCityForm
    template_name = "shopemanagement/createcity.html"
    success_url = "/shop/allcities/"

    def post(self, request, *args, **kwargs):
        self.object = None
        return super().post(request, *args, **kwargs)

    # def post(self, request, *args, **kwargs):
    #     if request.user.user_roll == 'm':
    #         self.object = None
    #         print("i am in user manager\n/n/", request.user.user_roll)
    #         return  super().post(self, request, *request, **kwargs)
    #     else:
    #         return response("you are not allowd to create city")


class UpdateCity(UpdateView):
    model = City
    template_name = "shopemanagement/createcity.html"
    fields = "__all__"
    success_url = "/shop/allcities/"


class DeleteCity(DeleteView):
    model = City
    template_name = "shopemanagement/delete_confirmation.html"
    success_url = "/shop/allcities/"


class AreaZoneListView(ListView):
    model = AreaZone
    template_name = "shopemanagement/allareazone.html"
    # paginate_by = 2

    def get_queryset(self):
        areazones = AreaZone.objects.all()
        search_parm = self.request.GET.get("search_field")
        print(type(search_parm))
        if search_parm:
            if search_parm.isdigit():
                search_parm = int(search_parm)
                areazones = AreaZone.objects.filter(pincode__icontains=search_parm)
                return areazones

            elif AreaZone.objects.filter(name__icontains=search_parm):
                areazones = AreaZone.objects.filter(name__icontains=search_parm)
                return areazones

            elif City.objects.filter(name__icontains=search_parm):
                city = City.objects.filter(name__icontains=search_parm).first()
                areazones = AreaZone.objects.filter(city=city)
                return areazones

            else:
                city = None
                areazones = AreaZone.objects.filter(city=city)
                return areazones
        return areazones

class CreateAreaZone(CreateView):
    model = AreaZone
    fields = ['name','city', 'pincode']
    success_url = "/shop/allareazones/"
    template_name = "shopemanagement/createareazone.html"


class UpdateAreaZone(UpdateView):
    model = AreaZone
    fields = "__all__"
    success_url = "/shop/allareazones/"
    template_name = "shopemanagement/createareazone.html"


class DeleteArea(DeleteView):
    model = AreaZone
    template_name = "shopemanagement/delete_confirmation.html"
    success_url = "/shop/allareazones/"



class CreateShop(CreateView):
    model = Shop


from django.contrib import admin

from shop.models import AreaZone, City


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    ordering = ("id",)
    list_filter = ("id", "name", "code")


@admin.register(AreaZone)
class AreaZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "pincode")
    list_filter = ("name", "city", "pincode")
    ordering = ("name",)

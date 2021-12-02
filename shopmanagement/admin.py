from django.contrib import admin

from shopmanagement.models import City, AreaZone


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


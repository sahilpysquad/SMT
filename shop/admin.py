from django.contrib import admin

from shop.models import AreaZone, City, CleaningGroup, Shop, ShopCategory, ShopHistory, Tax, Worker, SmtUsers


class AreaZoneTabularInline(admin.TabularInline):
    model = AreaZone


@admin.register(AreaZone)
class AreaZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "pincode")
    list_filter = ("name", "city", "pincode")
    ordering = ("name",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    ordering = ("id",)
    list_filter = ("id", "name", "code")
    inlines = [AreaZoneTabularInline]


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ("tax_name", "percentage")
    ordering = ("tax_name",)


@admin.register(ShopCategory)
class ShopCategoryAdmin(admin.ModelAdmin):
    pass
    list_display = ("category_name",)
    # ordering = ("name",)


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    # list_display = ()
    ordering = ("name",)


@admin.register(ShopHistory)
class ShopHistoryAdmin(admin.ModelAdmin):
    ordering = ("shop",)


@admin.register(CleaningGroup)
class CleaningGroupAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ("name",)


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    ordering = ("name",)


@admin.register(SmtUsers)
class SmtUserInternal(admin.ModelAdmin):
    list_display = ("user_roll", "supervisor", "area", "city")
    list_filter = ("user_roll", "city", "area")
    ordering = ("user_roll",)

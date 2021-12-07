from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class City(models.Model):
    name = models.CharField(max_length=30, unique=True)
    code = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


class AreaZone(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="cities")
    pincode = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SmtUsers(CommonInfo):
    TYPE_USER = [
            ('a', 'Manager'),
            ('s', 'Supervisor'),
            ('as', 'Assistant Supervisor'),
            ('o', 'Owner'),
    ]
    user_roll = models.CharField(choices=TYPE_USER, max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="user_cities")
    area = models.ForeignKey(AreaZone, on_delete=models.CASCADE, related_name="user_areas", null=True, blank=True)
    supervisor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="supervisors")

    def __str__(self):
        return self.name


class Tax(models.Model):
    tax_name = models.CharField(max_length=30)
    percentage = models.IntegerField()

    def __str__(self):
        return self.tax_name


class ShopCategory(models.Model):
    category_name = models.CharField(max_length=50)
    tax = models.ManyToManyField(Tax, related_name="taxes")

    def __str__(self):
        return self.category_name


class Shop(CommonInfo):
    SHOP_STATUS_CHOICES = (
        ("A", "Accepted"),
        ("P", "Pending"),
        ("C", "Canceled"),
    )
    shop_category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    owner = models.ForeignKey(SmtUsers, on_delete=models.CASCADE, related_name="owners", null=True, blank=True)
    assistant_supervisor = models.ForeignKey(SmtUsers, on_delete=models.CASCADE, related_name="assistants", null=True, blank=True)
    shop_status = models.CharField(max_length=1, choices=SHOP_STATUS_CHOICES, default="P")

    def __str__(self):
        return self.name


class ShopHistory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shops")

    def __str__(self):
        return self.shop


class CleaningGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    total_worker = models.IntegerField()
    next_day = models.DateTimeField()
    area = models.ForeignKey(AreaZone, on_delete=models.CASCADE, related_name="areas")

    def __str__(self):
        return self.name


class CleaningRecord(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_records")
    cleaning_date = models.DateTimeField()
    cleaning_range = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    cleaning_group = models.ForeignKey(CleaningGroup, on_delete=models.CASCADE, related_name="cleaning_groups")


class Worker(CommonInfo):
    WORKER_CHOICES = (
        ("C", "Cleaner"),
        ("E", "Employee")
    )

    VACCINE_DOSE_CHOICES = (
        (0, "Not Vaccinated"),
        (1, "One Dose"),
        (2, "Two Dose")
    )
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="worker_shops", null=True, blank=True)
    cleaning_group = models.ForeignKey(CleaningGroup, on_delete=models.CASCADE, related_name="cleaning_groups_worker", null=True, blank=True)
    worker_choice = models.CharField(max_length=1, choices=WORKER_CHOICES)
    vaccine_dose = models.IntegerField(choices=VACCINE_DOSE_CHOICES)

    def __str__(self):
        return self.name

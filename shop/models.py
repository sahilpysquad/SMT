from django.db import models


class City(models.Model):
    name = models.CharField(max_length=30, unique=True)
    code = models.IntegerField()

    def __str__(self):
        return self.name


class AreaZone(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
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


class Tax(models.Model):
    tax_name = models.CharField(max_length=30)
    percentage = models.IntegerField()

    def __str__(self):
        return self.tax_name


class ShopCategory(models.Model):
    category_name = models.CharField(max_length=50)
    tax = models.ManyToManyField(Tax)

    def __str__(self):
        return self.category_name


class Shop(CommonInfo):
    shop_category = models.ForeignKey(ShopCategory, on_delete=models.CASCADE)
    # owner = models.ForeignKey(on_delete=models.CASCADE)
    # assistant_supervisor = models.ForeignKey(on_delete=models.CASCADE)
    #total_worker = models.IntegerField()

    def __str__(self):
        return self.name


class ShopHistory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.shop


class CleaningGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    total_worker = models.IntegerField()
    next_day = models.DateTimeField()
    area = models.ForeignKey(AreaZone, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    cleaning_group = models.ForeignKey(CleaningGroup, on_delete=models.CASCADE)
    worker_choice = models.CharField(max_length=1, choices=WORKER_CHOICES)
    vaccine_dose = models.IntegerField(choices=VACCINE_DOSE_CHOICES)

    def __str__(self):
        return self.name

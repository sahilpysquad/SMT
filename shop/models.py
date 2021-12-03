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

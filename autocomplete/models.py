from django.db import models

from django.contrib.auth.models import User

class Test(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey("autocomplete.Country", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50)
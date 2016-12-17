from django.db import models


class Continent(models.Model):
    """ Write your answer in 7.1 here. """
    name = models.CharField(max_length=20,unique=True)
    code = models.CharField(max_length=2,unique=True)

    class Meta:
        ordering = ["name"]


class Country(models.Model):
    """ Write your answer in 7.1 here. """
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=2,unique=True)
    capital = models.CharField(max_length=100)
    population = models.PositiveIntegerField(default=0)
    area = models.PositiveIntegerField(default=0)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, related_name='countries')

    class Meta:
        ordering = ["name"]

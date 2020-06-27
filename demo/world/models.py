from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=2, help_text='Two letter continent code')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Country(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=2, help_text='ISO 3166-1 alpha-2 - two character country code')
    independence_day = models.DateField(blank=True, null=True)
    continent = models.ForeignKey(Continent, null=True, on_delete=models.SET_NULL)
    area = models.BigIntegerField(blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True, help_text='Try and enter few some more lines')
    architecture = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Countries"


class City(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    capital = models.BooleanField()
    area = models.BigIntegerField(blank=True, null=True)
    population = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cities"
        unique_together = ('name', 'country')

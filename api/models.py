from django.db import models


class CovidData(models.Model):
    fips = models.CharField(max_length=100, blank=True, null=True)
    admin2 = models.CharField(max_length=100, blank=True, null=True)
    province_state = models.CharField(max_length=100, blank=True, null=True)
    country_region = models.CharField(max_length=100, blank=True, null=True)
    last_updated = models.DateTimeField()
    lattitude = models.CharField(max_length=100, blank=True, null=True)
    longtitude = models.CharField(max_length=100, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    confirmed_cases = models.CharField(max_length=100, blank=True, null=True)
    deaths = models.CharField(max_length=100, blank=True, null=True)
    recovered = models.CharField(max_length=100, blank=True, null=True)
    active = models.CharField(max_length=100, blank=True, null=True)
    combined_key = models.CharField(max_length=100, blank=True, null=True)
    incident_rate = models.CharField(max_length=100, blank=True, null=True)
    case_fatality_ratio = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.country_region

from rest_framework import serializers

from api.models import CovidData


class CovidDataSerializer(serializers.ModelSerializer):
    deaths = serializers.IntegerField()
    # recovered = serializers.IntegerField()
    # active = serializers.IntegerField()
    # last_updated = serializers.DateField()

    class Meta:
        model = CovidData
        fields = ['deaths', 'fips', 'admin2', 'province_state', 'country_region', 'last_updated', 'lattitude',
                  'longtitude', 'confirmed_cases', 'recovered', 'active', 'combined_key', 'incident_rate', 'case_fatality_ratio', ]

from django.shortcuts import render
from django.views.generic import View
from api.serializers import CovidDataSerializer
from api.models import CovidData
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import timedelta, date


class IndexView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'api/index.html', context)


class QuickStart(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'api/quick-start.html', context)


class CovidDataView(APIView):
    def get(self, request, *args, **kwargs):
        covid_data = CovidData.objects.filter(
            province_state="Alabama",
            country_region="US").order_by('-last_updated')[:7]
        # serialize = CovidDataSerializer(covid_data,)
        # covid_data = get_covid_data()
        serialize = CovidDataSerializer(covid_data, many=True)
        return Response(serialize.data)

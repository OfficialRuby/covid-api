from rest_framework import status
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
        covid_data = CovidData.objects.all().order_by('-last_updated')[:7]
        serialize = CovidDataSerializer(covid_data, many=True)
        return Response(
            {'status': status.HTTP_200_OK,
                'message': 'Request successful',
             'data': serialize.data}
        )
        # return Response(serialize.data)

    def post(self, request, *args, **kwargs):
        params = request.POST
        lenght = 7
        # Chek if user provided a filter lenght
        if 'lenght' in params:
            lenght = params.get('lenght')
        # Check if user has provided date filter
        if 'data_from' and 'data_to' in params:
            param = params.copy()
            start_date = param.get('data_from')
            end_date = param.get('data_to')
            del param['data_from']
            del param['data_to']

            covid_data = CovidData.objects.filter(last_updated__range=(start_date, end_date),)
            if param:
                for key in param:
                    print('\n\n')
                    print(key)
                    print('\n\n')
                    listed = [key]
                    covid_data = covid_data.filter(key=params[key])

        serialize = CovidDataSerializer(covid_data, many=True)
        return Response(
            {'status': status.HTTP_200_OK,
                'message': 'Request successful',
             'data': serialize.data}
        )

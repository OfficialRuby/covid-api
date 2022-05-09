from django.core.exceptions import FieldError
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
        # Check if user has provided date filter
        if 'data_from' and 'data_to' in params:
            param = params.copy()
            start_date = param.get('data_from')
            end_date = param.get('data_to')
            del param['data_from']
            del param['data_to']

            covid_data = CovidData.objects.filter(last_updated__range=(start_date, end_date),)
            if param:
                try:
                    for key in param:
                        covid_data = covid_data.filter(**{key: param.get(key)})
                    if covid_data:
                        serialize = CovidDataSerializer(covid_data, many=True)
                        return Response(
                            {'status': status.HTTP_200_OK,
                                'message': 'Request successful',
                                'data': serialize.data}
                        )
                except FieldError:

                    return Response(
                        {'status': status.HTTP_400_BAD_REQUEST,
                         'message': 'Bad request',
                         'data': 'Please provide a valid parameter'}
                    )

        # Else perform a regular filtering
        else:
            # Chek if user provided a filter lenght
            param = params.copy()
            if 'lenght' in param:
                lenght = param.pop('lenght')
                lenght = int(lenght[0])
            if param:
                try:
                    for key in param:
                        covid_data = CovidData.objects.filter(**{key: param.get(key)})[:lenght]
                    if covid_data:
                        if len(covid_data) >= 1:
                            serialize = CovidDataSerializer(covid_data, many=True)
                        else:
                            serialize = CovidDataSerializer(covid_data,)
                        return Response(
                            {'status': status.HTTP_200_OK,
                                'message': 'Request successful',
                                'data': serialize.data}
                        )
                except FieldError as e:
                    return Response(
                        {'status': status.HTTP_400_BAD_REQUEST,
                         'message': 'Bad request',
                         'data': 'Please provide a valid parameter'}
                    )

        return Response(
            {'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Bad request',
                'data': 'Please provide a valid parameter'}
        )

from django.urls import path
from api.views import (IndexView, CovidDataView)


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('api/covid-data/', CovidDataView.as_view(), name='stat'),

]

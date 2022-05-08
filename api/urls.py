from django.urls import path
from api.views import (IndexView, CovidDataView, QuickStart)


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('doc/', QuickStart.as_view(), name='doc'),
    path('api/covid-data/', CovidDataView.as_view(), name='stat'),

]

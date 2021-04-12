from django.urls import path
from .views import BloombergDashAPI
from .dash_apps import bloomberg_dash


urlpatterns = [
    path('bloomberg_dash_api.html', BloombergDashAPI, name='bloomberg-dash'),
    ]

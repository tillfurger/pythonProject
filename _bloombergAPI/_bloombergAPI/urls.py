from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


def HomePage(request):
    return render(request, 'home.html', {})


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', HomePage, name='home'),
    path('api/', include('api.urls')),
    path('dash_api/', include('dash_api.urls')),
    path('django_plotly_dash/', include('django_plotly_dash.urls'))
]

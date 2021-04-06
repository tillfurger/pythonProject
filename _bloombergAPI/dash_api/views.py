from django.shortcuts import render


def BloombergDashAPI(request):
    return render(request, 'dash_api/bloomberg_dash_api.html', {})

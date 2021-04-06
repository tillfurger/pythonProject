from django.shortcuts import render
from .forms import BBForm
from xbbg import blp


def BloombergAPI(request):
    if request.method == 'GET':
        form = BBForm()
        context = {'form': form}
        return render(request, 'api/bloomberg_api.html', context)

    elif request.method == "POST":
        form = BBForm(request.POST)
        if form.is_valid():
            ticker = form.cleaned_data['ticker']
            variable = form.cleaned_data['variable']
            start = form.cleaned_data['start_date'].strftime('%Y-%m-%d')
            end = form.cleaned_data['end_date'].strftime('%Y-%m-%d')
            form = BBForm()
            ts = blp.bdh(ticker, variable, start, end)
            data = ts[ticker][variable].to_list()
            labels = ts.index.strftime('%Y-%m-%d').to_list()
            context = {'form': form, 'data': data, 'labels': labels, 'variable': variable, 'ticker': ticker}
        return render(request, 'api/bloomberg_api.html', context)

    else:
        return render(request, 'api/bloomberg_api.html', {})


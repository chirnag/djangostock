from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Stock
from .forms import StockForm
from django.contrib import messages

# Create your views here.

def home(request):
    import requests 
    import json
    # pk_adc0c18f6fdf474a8c1ba9784af51d79
    if request.method == 'POST':
        ticker = request.POST['ticker']
        try:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote/?token=pk_adc0c18f6fdf474a8c1ba9784af51d79")
            api = json.loads(api_request.content)
        except Exception as identifier:
            api = "Error"        
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker symbol above"})    

    

def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    import requests
    import json

    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('add_stock')
    else:
        tickers = Stock.objects.all()
        output = []
        for ticker_item in tickers:
            try:
                api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + str(ticker_item) + "/quote/?token=pk_adc0c18f6fdf474a8c1ba9784af51d79")
                api_response = json.loads(api_request.content)
                output.append(api_response)
            except Exception as exception:
                api_response = "Error"
        return render(request, 'add_stock.html', {'tickers': tickers, "output": output, "api_response": api_response})

def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted"))
    return redirect(add_stock)

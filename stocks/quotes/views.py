from django.shortcuts import render

# Create your views here.

def home(request):
    import requests 
    import json
    # pk_adc0c18f6fdf474a8c1ba9784af51d79
    
    try:
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote/latestPrice?token=pk_adc0c18f6fdf474a8c1ba9784af51d79")
        api = json.loads(api_request.content)
    except Exception as identifier:
        api = identifier        

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})

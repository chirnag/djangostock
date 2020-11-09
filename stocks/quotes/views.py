from django.shortcuts import render

# Create your views here.

def home(request):
    # pk_adc0c18f6fdf474a8c1ba9784af51d79
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

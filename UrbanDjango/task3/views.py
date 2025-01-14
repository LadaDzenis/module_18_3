from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'masloDzen.html')

def price(request):
    return render(request, 'prices_maslo.html')

def disc(request):
    return render(request, 'description_maslo.html')
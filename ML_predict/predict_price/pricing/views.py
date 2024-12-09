from django.shortcuts import render
from .scrapers.yelp_scraper import fetch_village_data

def get_village_data(request):
    # Fetch data from Yelp
    village_data = fetch_village_data()
    
    if village_data:
        context = {
            'village_data': village_data
        }
        return render(request, 'restaurant_template.html', context)
    else:
        return render(request, 'error.html', {'message': 'Failed to fetch data from Yelp'})

# pricing/views.py
from django.http import HttpResponse

def restaurant_view(request):
    return HttpResponse("Restaurant data goes here!")

# pricing/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Home Page!")

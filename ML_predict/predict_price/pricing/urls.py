from django.urls import path
from . import views
from .views import restaurant_view

urlpatterns = [
    path('scrape/village/', views.get_village_data, name='get_village_data'),
    path('restaurant/', restaurant_view, name='restaurant'),
    # You can add more paths for other features in the 'pricing' app if needed
]

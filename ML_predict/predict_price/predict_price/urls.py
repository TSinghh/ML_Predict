from django.contrib import admin
from django.urls import path, include
from pricing import views  # Import views from the 'pricing' app for the homepage
# predict_price/urls.py
from pricing.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pricing/', include('pricing.urls')), 
    path('village/', views.get_village_data, name='village_data'),  # This will map to the get_village_data view
    path('', views.home, name='home'),  # Add the home view for the root URL
]

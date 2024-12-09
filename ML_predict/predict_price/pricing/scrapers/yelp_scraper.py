# predict_price/scrapers/yelp_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_village_data():
    # URL of the Yelp page
    url = "https://www.yelp.com/menu/village-the-soul-of-india-hicksville"
    
    # Send a GET request to fetch the page content
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Example: Find all menu items (you will need to adjust this based on Yelp's HTML structure)
        menu_items = soup.find_all('div', class_='menu-item')  # Adjust this based on actual page structure
        
        menu_data = []
        for item in menu_items:
            name = item.find('h3').text.strip()  # Get item name
            price = item.find('span', class_='price').text.strip()  # Get item price
            
            menu_data.append({'name': name, 'price': price})
        
        return menu_data
    else:
        return None

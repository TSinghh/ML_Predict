# ML_Predict

# Village Pricing Prediction
This project is a Django-based application that predicts menu prices for "Village The Soul of India" based on weather, busyness, and surrounding restaurant prices. The project integrates multiple APIs, uses an ML algorithm for price prediction, and displays outputs via a webpage.

Features
1. API Integration:
Google Places API: Fetch restaurant details and nearby top-rated restaurants.
OpenWeatherMap API: Fetch weather data including temperature and rainfall.

3. Price Prediction:Machine Learning model adjusts menu prices based on weather, busyness, and surrounding prices.

# How to run the code
To run the project, start by cloning the repository from GitHub and navigating into the project directory. Set up a Python virtual environment using `python -m venv venv` and activate it (`venv\Scripts\activate` on Windows or `source venv/bin/activate` on macOS/Linux). Install the required libraries using `pip install -r requirements.txt`. Next, create a `.env` file in the root directory and add your API keys for Google Cloud (`GOOGLE_API_KEY`) and OpenWeather (`OPENWEATHER_API_KEY`). Run `python manage.py migrate` to set up the Django database, then start the server with `python manage.py runserver`. Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application and its outputs. Ensure you have an active internet connection for API functionality, and test using Django's development server or shell if needed.

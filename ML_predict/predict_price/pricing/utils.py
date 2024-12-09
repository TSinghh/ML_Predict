def adjust_prices(menu, temperature, rain):
    adjusted_menu = []
    
    for item in menu:
        price = item["price"]
        
        # Example adjustment based on weather:
        if temperature > 30:  # Hot weather
            price += 2  # Increase price by 2 for hot weather
        elif rain > 0:  # Rainy weather
            price -= 1  # Decrease price by 1 for rainy weather
        
        adjusted_menu.append({**item, "adjusted_price": price})
    
    return adjusted_menu

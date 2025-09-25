import requests
import json
from datetime import datetime

def fetch_hk_temperature():
    """
    Fetch current temperature data from Hong Kong Observatory API
    Returns the current temperature in Celsius
    """
    # Official HKO API endpoint for current weather
    API_ENDPOINT = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"
    
    try:
        response = requests.get(API_ENDPOINT, timeout=5)  # Add timeout
        if response.status_code == 200:
            data = response.json()
            # The API returns temperature data for multiple stations
            # We'll use the Hong Kong Observatory (station_code='HKO') reading
            temp_data = data.get('temperature', {}).get('data', [])
            
            # Try to get HKO station data first
            for station in temp_data:
                if station.get('place') == 'Hong Kong Observatory':
                    temp = station.get('value')
                    if temp is not None:
                        return float(temp)
            
            # If HKO station not found, try King's Park station
            for station in temp_data:
                if station.get('place') == "King's Park":
                    temp = station.get('value')
                    if temp is not None:
                        return float(temp)
            
            # If neither station found, use any available station
            for station in temp_data:
                temp = station.get('value')
                if temp is not None:
                    return float(temp)
            
        print("Warning: Could not fetch temperature data, using default value")
        return 25
    except Exception as e:
        print(f"Error fetching temperature data: {e}")
        return 25  # Default temperature in Celsius

def get_temperature_category(temp):
    """
    Categorize temperature into different ranges
    """
    if temp < 15:
        return 'cold'
    elif temp < 22:
        return 'moderate'
    elif temp < 28:
        return 'warm'
    else:
        return 'hot'
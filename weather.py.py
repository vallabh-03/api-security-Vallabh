import os
from dotenv import load_dotenv
import requests

# Load API key securely from .env - never hardcode [Task 1]
load_dotenv()
api_key = os.getenv('OPENWEATHER_API_KEY')

if not api_key:
    print("ERROR: OPENWEATHER_API_KEY missing from .env file")
    exit(1)

base_url = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch current weather with proper error handling.
    """
    # Do NOT log city name - violates patient location privacy 
    # under India's DPDP Act 2023 (Section 8: data minimization) 
    # and GDPR Art 25 (privacy by design) [Task 3]
    # pass  # Generic processing indicator only
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        
        # Handle rate limiting gracefully [Task 2]
        if response.status_code == 429:
            print("Rate limit exceeded (60 calls/min free tier). Wait 1 minute and try again.")
            return None
            
        # Handle other HTTP errors
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('cod') != 200:
            print(f"Weather data unavailable: {data.get('message', 'Unknown error')}")
            return None
            
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"Current temperature: {temp}°C, {description.title()}")
        return data
        
    except requests.exceptions.Timeout:
        print("Request timeout. Please try again.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Network error: {str(e)}")
        return None
    except KeyError as e:
        print("Invalid API response format. Check API key and endpoint.")
        return None
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    if city:
        get_weather(city)
import requests

API_KEY = "d871280b8eb5a48ae516fc3e0744912c"
BASE_URL = "https://api.openweathermap.org/data/2.5/"

def get_weather(city):
    """Fetch current weather data for a given city (Fahrenheit)."""
    url = f"{BASE_URL}weather?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    else:
        return {"error": f"Error fetching data: {response.status_code}"}

def get_forecast(city):
    """Fetch 5-day weather forecast for a given city (Fahrenheit)."""
    url = f"{BASE_URL}forecast?q={city}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        forecast_list = []
        for forecast in data["list"][:5]:  # Get first 5 forecast entries
            forecast_list.append({
                "date_time": forecast["dt_txt"],
                "temperature": forecast["main"]["temp"],
                "weather": forecast["weather"][0]["description"],
                "wind_speed": forecast["wind"]["speed"]
            })
        return forecast_list
    else:
        return {"error": f"Error fetching data: {response.status_code}"}

if __name__ == "__main__":
    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()
        
        if city.lower() == "exit":
            print("Exiting program. Goodbye!")
            break
        
        weather = get_weather(city)
        if "error" in weather:
            print(weather["error"])
        else:
            print(f"\nCurrent Weather in {weather['city']}:")
            print(f"Temperature: {weather['temperature']}°F")
            print(f"Condition: {weather['weather']}")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Wind Speed: {weather['wind_speed']} mph")

            print("\n5-Day Forecast:")
            forecast = get_forecast(city)
            if "error" in forecast:
                print(forecast["error"])
            else:
                for day in forecast:
                    print(f"{day['date_time']}: {day['temperature']}°F, {day['weather']}, Wind: {day['wind_speed']} mph")
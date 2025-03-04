import requests
import geocoder
import json
import os

# WeatherAPI Key (Replace with your actual API key)
API_KEY = "8082f4a780034775bf5112531250403"

# Step 1: Get System Location
def get_location():
    g = geocoder.ip("me")  # Gets public IP-based location
    if g.ok:
        return g.latlng  # Returns (latitude, longitude)
    else:
        print("❌ Could not determine location.")
        return None

# Step 2: Fetch Weather Data from API
def get_weather(lat, lon):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lon}&aqi=no"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # Return parsed JSON data
    else:
        print(f"❌ API Error: {response.status_code}")
        return None

# Step 3: Save Weather Data to JSON File
def save_to_json(data, filename="weather_data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"✅ Weather data saved to {filename}")

# Step 4: Save Weather Data to Text File
def save_to_text(data, filename="weather_data.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"📍 Location: {data['location']['name']}, {data['location']['country']}\n")
        file.write(f"🌡️ Temperature: {data['current']['temp_c']}°C\n")
        file.write(f"☁️ Condition: {data['current']['condition']['text']}\n")
        file.write(f"💨 Wind Speed: {data['current']['wind_kph']} kph\n")
        file.write(f"🌧️ Humidity: {data['current']['humidity']}%\n")
    print(f"✅ Weather data saved to {filename}")

# Step 5: Main Function to Run the App
def main():
    location = get_location()
    if location:
        lat, lon = location
        print(f"📍 Detected Location: Latitude {lat}, Longitude {lon}")
        
        weather_data = get_weather(lat, lon)
        if weather_data:
            save_to_json(weather_data)
            save_to_text(weather_data)
        else:
            print("❌ Could not fetch weather data.")

# Run the app
if __name__ == "__main__":
    main()

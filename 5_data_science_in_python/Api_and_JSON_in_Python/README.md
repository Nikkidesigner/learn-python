# Working with APIs and JSON in Python



## **1. Introduction to APIs**

### **What is an API?**
An **Application Programming Interface (API)** is a communication bridge between software applications. APIs allow developers to interact with external services, retrieve or send data, and perform operations programmatically.


<p align="center"> 
<img  src="https://github.com/user-attachments/assets/98b54169-a015-4d0f-8a62-85bebc9776c5" alt="Material Bread logo">
</p>

### **Components of a Web API**
A Web API generally consists of:
1. **HTTP Protocol** - APIs use HTTP methods like GET, POST, PUT, and DELETE.
2. **Data Format (JSON/XML)** - API responses are usually formatted as JSON.
3. **Endpoints** - Specific URLs that allow data interaction (e.g., `/api/courses`).
4. **Authentication** - APIs often require API keys or OAuth tokens for security.

---


![image](https://github.com/user-attachments/assets/9a3d8013-59b6-4a3b-9d0e-167f41dd852d)




### **Public vs Private APIs**
- **Public APIs** - Open to the public, meant for developers (e.g., OpenWeatherMap API).
- **Private APIs** - Restricted for internal use by an organization (e.g., LearnCodeTheHardWay API).

---

## **2. Understanding JSON (JavaScript Object Notation)**

### **What is JSON and Why is it Used?**
JSON is a lightweight, human-readable data exchange format widely used for APIs. It is easy to parse, platform-independent, and maps directly to Python dictionaries.

### **JSON vs Other Data Formats**
| Feature         | JSON  | XML  | YAML  |
|---------------|------|------|------|
| Readability   | ✅ Easy  | ❌ Verbose | ✅ Very Easy |
| Parsing Speed | ✅ Fast | ❌ Slower  | ✅ Fast |
| Human-Readable | ✅ Yes  | ✅ Yes  | ✅ Yes |

### **JSON Syntax**
```json
{
  "name": "Python Course",
  "modules": [
    {"id": 1, "title": "Introduction"},
    {"id": 2, "title": "APIs & JSON"}
  ],
  "published": true
}
```

---

## **3. Working with JSON in Python**

### **Python's `json` Module**
Python provides a built-in `json` module for handling JSON data.

### **Convert Python Dictionary to JSON (Serialization)**
```python
import json

data = {"course": "Python API", "level": "Intermediate"}
json_string = json.dumps(data)
print(json_string)  # Output: {"course": "Python API", "level": "Intermediate"}
```

### **Convert JSON to Python Dictionary (Deserialization)**
```python
json_data = '{"course": "Python API", "level": "Intermediate"}'
python_dict = json.loads(json_data)
print(python_dict["course"])  # Output: Python API
```

### **Read/Write JSON Files**
```python
# Writing JSON to a file
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading JSON from a file
with open("data.json", "r") as file:
    content = json.load(file)
print(content)
```

---

## **4. Accessing APIs with Python (`requests` Module)**

### **Install `requests`**
```sh
conda activate lpythw
conda install requests
```

### **Making API Requests**
```python
import requests

api_url = "https://learncodethehardway.com/api/course"
response = requests.get(api_url)
print(response.json())  # Print JSON response
```

### **Caching API Responses**
```python
import os

if not os.path.exists("courses.json"):
    with open("courses.json", "w") as file:
        json.dump(response.json(), file)
```

---

## **5. Practical API Example: Extracting Watch Time**

### **Understanding the API Structure**
The LearnCodeTheHardWay API has the following endpoints:
- `/api/course` → List of courses
- `/api/module` → List of modules in a course
- `/api/lesson` → List of lessons in a module
- `/api/lesson_media` → Media details for lessons

### **Extracting Watch Time**
```python
import requests
import csv

api_url = "https://learncodethehardway.com/api/course"
response = requests.get(api_url)
courses = response.json()

with open("watch_time.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Course", "Total Minutes"])
    
    for course in courses:
        total_minutes = sum(lesson["duration"] for lesson in course["lessons"])
        writer.writerow([course["title"], total_minutes])
```

---

## **6. Advanced API Techniques**

### **Using `FastAPI` for API Development**
```python
from fastapi import FastAPI
app = FastAPI()

@app.get("/api/course")
def get_courses():
    return [{"id": 1, "title": "Learn Python"}]
```

### **Querying JSON with `jq`**
```sh
curl https://learncodethehardway.com/api/course | jq '.'
```

### **Testing APIs with `curl`**
```sh
curl -X GET https://learncodethehardway.com/api/module?course_id=1
```

---

## **7. Best Practices for Working with APIs**

### **Error Handling and Logging**
```python
try:
    response = requests.get(api_url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"API Error: {e}")
```

### **Rate Limiting & Avoiding API Abuse**
- Use caching to minimize API calls.
- Respect API rate limits (check API documentation).
- Implement retries with exponential backoff.

### **Security Considerations**
- Never hardcode API keys in your code.
- Use environment variables to store credentials.
- Ensure API endpoints use HTTPS.


---

## **📌 Key Takeaways**
✅ APIs allow seamless communication between applications.  
✅ JSON is the most commonly used data format for APIs.  
✅ Python’s `requests` module simplifies API interactions.  
✅ Always cache API responses to reduce unnecessary requests.  
✅ Follow best practices for security and error handling.  

With these skills, you're now equipped to **interact with APIs, process JSON data, and automate workflows! 🚀**






# **📌 Project: Weather App Using System Location & API**  
This application **automatically fetches the user's location**, sends it to the **Weather API**, retrieves **current weather data**, and stores it in both **JSON and text files**.  

---

# **📌 Features of the App**
✅ **Detects system location (Latitude & Longitude)**  
✅ **Fetches weather details from WeatherAPI**  
✅ **Saves weather data to JSON & text files**  
✅ **Handles errors (e.g., network issues, invalid API key)**  

---

## **📌 Install Required Libraries**
Before running the script, install the necessary libraries:
```bash
pip install requests geocoder
```
---

# **📌 Full Python Code (Copy & Paste to Run)**
```python
import requests
import geocoder
import json
import os

# WeatherAPI Key (Replace with your actual API key)  GET YOUR API FROM HERE : https://www.weatherapi.com/docs/
API_KEY = "PASTE_YOUR_API_KEY"

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

```
---

# **📌 How the Code Works**
### ✅ **1. Get System Location**
```python
g = geocoder.ip("me")
location = g.latlng
```
- Uses **Geocoder** to get **latitude & longitude** of the system.
- Uses the **public IP address** to estimate the location.

---

### ✅ **2. Fetch Weather Data**
```python
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={lat},{lon}&aqi=no"
response = requests.get(url)
weather_data = response.json()
```
- Sends a **request to WeatherAPI** using the system's **latitude & longitude**.
- Retrieves **current weather details** as **JSON**.

---

### ✅ **3. Save Data to a JSON File**
```python
with open(filename, "w") as file:
    json.dump(data, file, indent=4)
```
- Saves **structured JSON data** into `weather_data.json`.

---

### ✅ **4. Save Data to a Text File**
```python
with open(filename, "w") as file:
    file.write(f"📍 Location: {data['location']['name']}, {data['location']['country']}\n")
    file.write(f"🌡️ Temperature: {data['current']['temp_c']}°C\n")
```
- Extracts **important weather details** and saves them in a **readable text file**.

---

### ✅ **5. Run the App**
```python
if __name__ == "__main__":
    main()
```
- Calls the `main()` function to:
  1. **Get location**
  2. **Fetch weather**
  3. **Save data to files**

---

# **📌 Example Output**
### ✅ **Console Output**
```
📍 Detected Location: Latitude 51.5074, Longitude -0.1278
✅ Weather data saved to weather_data.json
✅ Weather data saved to weather_data.txt
```

### ✅ **JSON File (`weather_data.json`)**
```json
{
    "location": {
        "name": "London",
        "region": "City of London, Greater London",
        "country": "United Kingdom"
    },
    "current": {
        "temp_c": 12.0,
        "condition": {
            "text": "Partly cloudy"
        },
        "wind_kph": 15.0,
        "humidity": 82
    }
}
```

### ✅ **Text File (`weather_data.txt`)**
```
📍 Location: London, United Kingdom
🌡️ Temperature: 12°C
☁️ Condition: Partly cloudy
💨 Wind Speed: 15 kph
🌧️ Humidity: 82%
```

---

# **📌 Concepts & Libraries Used**
| **Concept** | **Usage** |
|------------|------------|
| `requests.get()` | Fetches data from the WeatherAPI |
| `geocoder.ip("me")` | Gets system's latitude & longitude |
| `json.loads()` | Converts API response into Python dictionary |
| `json.dump()` | Saves data into a JSON file |
| `open(filename, "w")` | Writes data into a text file |

---

# **📌 How to Run the App**
### ✅ **1. Install Required Libraries**
```bash
pip install requests geocoder
```
### ✅ **2. Run the Script**
```bash
python weather_app.py
```

---

# **📌 Summary**
✅ **Detects system location using Geocoder**  
✅ **Fetches weather details from WeatherAPI**  
✅ **Saves results to JSON and text files**  
✅ **Handles errors gracefully**  

🚀 **Now, anyone can copy, paste, and run this app without modifications!** 🚀

Would you like to **add more weather details like sunrise/sunset or forecast**? 😊



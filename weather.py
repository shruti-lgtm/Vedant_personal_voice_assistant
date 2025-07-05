import requests
from ss import key2

city = "Mumbai"
api_address = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key2}"

try:
    response = requests.get(api_address, timeout=10)
    json_data = response.json()

    def temp():
        temperature = round(json_data["main"]["temp"] - 273.15, 1)
        return temperature

    def des():
        description = json_data["weather"][0]["description"]
        return description

except requests.exceptions.ConnectTimeout:
    print("Error: Connection to OpenWeather timed out.")
    def temp(): return "not available"
    def des(): return "not available"
except:
    print("Some other weather error occurred.")
    def temp(): return "not available"
    def des(): return "not available"

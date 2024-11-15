import requests

def get_weather():
    api_key = "c6d2834a60df2d305afed9f2857520c6"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # Ask the user for a municipality name
    city = input("Enter city name: ")
    params = {
        "q": city,
        "appid": api_key
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temperature_k = data['main']['temp']
        temperature_c = temperature_k - 273.15

        print(f"Weather condition: {weather_desc.capitalize()}")
        print(f"Temperature: {temperature_c:.2f} °C")
    else:
        print("Wrong city.")

get_weather()

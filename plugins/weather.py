import requests
from datetime import datetime

from config.settings import WEATHER_API_KEY
from core.groq_assistant import groq_assistant_object
from core.command_utils import extract_info_from_command

def initial_function_weather(command):
    prompt = f"""
        The text enclosed in angle brackets is a command given to a voice assistant:

        <{command}>

        Your task is to:
        1. Identify if a city name is mentioned in the command.
        2. If a city is mentioned, return only the name of the city (one word).
        3. If no city is mentioned, return literally the word "None".

        Output:
        Respond only with a JSON object using lowercase keys and proper casing for city names. The JSON must have exactly one key:
        - "city": a single word that is either the city name or "None"

        Rules:
        - No punctuation outside of the JSON syntax.
        - No explanations, no extra text, and no quotes around the JSON.
        - Output must follow this format exactly:

        {{ "city": "Kathmandu" }}
        or
        {{ "city": "None" }}
    """
    return extract_info_from_command(prompt)


def get_weather(extracted_info):

    city = extracted_info['city']

    if city == "None":        #Checks if city equals literally "None"
        city = 'Butwal'
    print(city)

    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        # print("[DEBUG] OpenWeather response:", data)

        if response.status_code != 200 or data.get("cod") != "200":
            message = f"Couldn't find forecast for {city}. Please try another city."
            print("[ERROR]", message)
            return message

        today_str = datetime.now().strftime("%Y-%m-%d")
        today_forecasts = [f for f in data["list"] if f["dt_txt"].startswith(today_str)]

        if not today_forecasts:
            return f"Sorry, no forecast found for today in {city}."

        forecast = today_forecasts[0]
        dt_txt = forecast["dt_txt"]
        desc = forecast["weather"][0]["description"]
        temp = forecast["main"]["temp"]
        feels_like = forecast["main"]["feels_like"]
        humidity = forecast["main"]["humidity"]

        weather_report = (
            f"The forecast in {city} at {dt_txt} is {desc}. "
            f"Temperature is {temp}°C, feels like {feels_like}°C, "
            f"with {humidity}% humidity."
            f"Thank you."
        )
        return weather_report
    
    except Exception as e:
        print("[EXCEPTION] Weather fetch error:", e)
        return "Sorry, I couldn't fetch the weather forecast."


import requests
from twilio.rest import Client
from datetime import datetime, timedelta

# Replace these with your actual API keys and phone numbers
OPENWEATHERMAP_API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
TWILIO_ACCOUNT_SID = "YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER = "YOUR_TWILIO_PHONE_NUMBER"
RECIPIENT_PHONE_NUMBER = input("Enter recipient's phone number: ")  # Prompt for recipient's phone number


def get_weather(city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": OPENWEATHERMAP_API_KEY,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)  # Print the API response for debugging
    return data


def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )
        print("SMS sent successfully!")
    except Exception as e:
        print("Error sending SMS:", e)


def main():
    city = input("Enter city name: ")
    weather_data = get_weather(city)

    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        humidity = weather_data["main"]["humidity"]
        wind_speed = weather_data["wind"]["speed"]

        # Calculate local time using the provided timezone offset
        timezone_offset = timedelta(seconds=weather_data["timezone"])
        current_time_utc = datetime.utcfromtimestamp(weather_data["dt"])  # UTC time from API
        local_time = current_time_utc + timezone_offset

        sunrise_time_utc = datetime.utcfromtimestamp(weather_data["sys"]["sunrise"])  # UTC sunrise time
        sunset_time_utc = datetime.utcfromtimestamp(weather_data["sys"]["sunset"])  # UTC sunset time

        sunrise_time = sunrise_time_utc + timezone_offset
        sunset_time = sunset_time_utc + timezone_offset

        pressure = weather_data["main"]["pressure"]
        visibility = weather_data.get("visibility", "N/A")

        message = (
            f"Current weather in {city}: {temperature}°C, {weather_description}\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s\n"
            f"Local Time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"Sunrise: {sunrise_time.strftime('%H:%M:%S')}\n"
            f"Sunset: {sunset_time.strftime('%H:%M:%S')}\n"
            f"Atmospheric Pressure: {pressure} hPa\n"
            f"Visibility: {visibility} meters"
        )
        send_sms(message)
    else:
        print("Failed to fetch weather data.")


if __name__ == "__main__":
    main()

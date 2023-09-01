# Send SMS Weather Notification

This script retrieves weather information from OpenWeatherMap API based on the user-provided city name and sends an SMS notification containing the weather details using the Twilio API.

## Prerequisites

Before using this script, you need to have the following:

- OpenWeatherMap API Key: Sign up on the [OpenWeatherMap website](https://openweathermap.org/) to obtain an API key.
- Twilio Account SID and Auth Token: Sign up on the [Twilio website](https://www.twilio.com/) to get your account SID and auth token.
- Python 3: Make sure you have Python 3 installed on your system.

## Installation

1. Clone this repository or download the script.

git clone https://github.com/CharlesFabicki/Send.SMS.Weather.Notification.git


2. Install the required Python packages using pip.
```bash
pip install requests twilio
```

3. Replace the placeholder API keys and phone numbers in the script with your actual values.

## Usage

1. Open a terminal and navigate to the directory where the script is located.

2. Run the script using the following command:

```bash
python weather_sms_notifier.py
```

3. Follow the prompts to enter the recipient's phone number and the city name for weather information.

4. The script will retrieve the weather data and send an SMS notification with the weather details to the provided phone number.

## Example

Enter recipient's phone number: +1234567890

Enter city name: New York

Current weather in New York: 25°C, Clear sky

Humidity: 60%

Wind Speed: 5.0 m/s

Local Time: 2023-08-29 14:30:00

Sunrise: 06:00:00

Sunset: 18:30:00

Atmospheric Pressure: 1015 hPa

Visibility: 10000 meters

SMS sent successfully!



## License

This project is licensed under the  License

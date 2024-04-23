import requests
import os


def get_api_key():
    try:
        with open('day-035/project-035_rain_alert/.config', 'r') as configFile:
            return configFile.readline()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


def check_for_rain(json_data):
    will_rain = False
    for hour in json_data["list"]:
        condition_code = hour["weather"][0]["id"]
        if int(condition_code) < 700:
            will_rain = True
    if will_rain:
        print("Bring an umbrella")


if __name__ == "__main__":
    os.environ["API_KEY"] = get_api_key()
    OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
    api_parameters = {
        "lon": 51.507351,
        "lat": -0.127758,
        "appid": os.environ["API_KEY"],
        "cnt": 4
    }

    response = requests.get(OWM_ENDPOINT, params=api_parameters)
    response.raise_for_status()

    weather_json = response.json()
    check_for_rain(weather_json)

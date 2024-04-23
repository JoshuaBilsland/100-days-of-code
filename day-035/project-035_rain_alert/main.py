import requests
import os


def get_api_key():
    try:
        with open('day-035/project-035_rain_alert/.config', 'r') as configFile:
            return configFile.readline()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


if __name__ == "__main__":
    os.environ["API_KEY"] = get_api_key()
    print(os.environ["API_KEY"])

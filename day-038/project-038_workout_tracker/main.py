import requests
from datetime import datetime


def get_api_key(line_num):
    try:
        with open('day-038/project-038_workout_tracker/.config', 'r') as configFile:
            lines = configFile.readlines()
            return lines[line_num].strip()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


def main():
    WEIGHT_KG = 65
    HEIGHT_CM = 175
    AGE = 19

    APP_ID = get_api_key(0)
    API_KEY = get_api_key(1)

    EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
    SHEET_ENDPOINT = get_api_key(2)

    user_exercise_input = input("Tell me which exercises you did: ")

    request_headers = {
        "Content-Type": "application/json",
        "x-app-id": APP_ID,
        "x-app-key": API_KEY
    }
    params = {
        "query": user_exercise_input,
        "weight_kg": WEIGHT_KG,
        "height_cm": HEIGHT_CM,
        "age": AGE
    }
    response = requests.post(url=EXERCISE_ENDPOINT,
                             headers=request_headers,
                             json=params)
    response.raise_for_status()
    json_response = response.json()

    # Add row to Google Sheets with Sheety API
    current_date = datetime.now()
    current_date = current_date.strftime("%d/%m/%Y")
    current_time = datetime.now()
    current_time = current_time.strftime("%X")

    for exercise in json_response["exercises"]:
        exercise_name = exercise["name"]
        duration_min = exercise["duration_min"]
        nf_calories = exercise["nf_calories"]

        sheet_params = {
            "workout": {
                "date": current_date,
                "time": current_time,
                "exercise": exercise_name.title(),
                "duration": duration_min,
                "calories": nf_calories
            }
        }
        sheet_response = requests.post(url=SHEET_ENDPOINT,
                                       headers=request_headers,
                                       json=sheet_params)
        sheet_response.raise_for_status()


if __name__ == "__main__":
    main()

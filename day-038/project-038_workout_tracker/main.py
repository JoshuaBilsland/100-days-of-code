import requests


def get_api_key(line_num):
    try:
        with open('day-038/project-038_workout_tracker/.config', 'r') as configFile:
            lines = configFile.readlines()
            return lines[line_num].strip()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


def main():
    WEIGHT_KG = YOUR_WEIGHT
    HEIGHT_CM = YOUR_HEIGHT
    AGE = YOUR_AGE

    APP_ID = get_api_key(0)
    API_KEY = get_api_key(1)

    EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
    print(response.json())


if __name__ == "__main__":
    main()

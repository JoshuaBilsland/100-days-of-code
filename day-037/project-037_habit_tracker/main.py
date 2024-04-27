import requests
from datetime import datetime

def get_api_key(line_num):
    try:
        with open('day-037/project-037_habit_tracker/.config', 'r') as configFile:
            lines = configFile.readlines()
            return lines[line_num].strip()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


def main():
    PIXELA_ENDPOINT = "https://pixe.la/v1/users"
    PIXELA_TOKEN = get_api_key(0)
    PIXELA_USERNAME = get_api_key(1)  # Stores username in .config
    PIXELA_GRAPH_ID = "graph1"

    user_params = {
        "token": PIXELA_TOKEN,
        "username": PIXELA_USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    # CREATING USER ACCOUNT
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response.text)

    # CREATING USER GRAPH
    graph_config = {
        "id": PIXELA_GRAPH_ID,
        "name": "Pages Read Graph",
        "unit": "Pages",
        "type": "int",
        "color": "momiji"

    }

    pixela_headers = {
        "X-USER-TOKEN": PIXELA_TOKEN
    }

    GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
    response = requests.post(
        url=GRAPH_ENDPOINT,
        json=graph_config,
        headers=pixela_headers
    )
    print(response.text)

    # POST A PIXEL
    POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH_ID}"
    today = datetime.now()

    pixel_params = {
        "date": today.strftime("%Y%m%d"),
        "quantity": "5"
    }
    response = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_params, headers=pixela_headers)
    print(response.text)

if __name__ == "__main__":
    main()

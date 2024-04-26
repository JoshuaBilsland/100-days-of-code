import requests


def get_api_key(line_num):
    try:
        with open('day-036/project-036_stock_news/.config', 'r') as configFile:
            lines = configFile.readlines()
            return lines[line_num].strip()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = get_api_key(0)


def main():
    user_params = {
        "token": PIXELA_ENDPOINT,
        "username": "joshb109",
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response.text)
    response.raise_for_status()



if __name__ == "__main__":
    main()

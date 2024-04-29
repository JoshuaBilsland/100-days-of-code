def get_api_key(line_num):
    try:
        with open('day-037/project-037_habit_tracker/.config', 'r') as configFile:
            lines = configFile.readlines()
            return lines[line_num].strip()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


def main():
    APP_ID = get_api_key(0)
    API_KEY = get_api_key(1)


if __name__ == "__main__":
    main()

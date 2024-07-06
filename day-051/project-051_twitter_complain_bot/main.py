from selenium import webdriver


def get_config_key(line_num):
    try:
        with open('day-049/project-049_linkedin_automation/.config', 'r') as configFile:
            lines = configFile.readlines()
            return lines[line_num].strip()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)

        self.__driver = webdriver.Chrome(options=chrome_options)
        self.__down = 0
        self.__up = 0

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


def main():
    bot = InternetSpeedTwitterBot()
    bot.get_internet_speed()
    bot.tweet_at_provider()


if __name__ == "__main__":
    PROMISED_DOWN = 150
    PROMISED_UP = 10
    TWITTER_EMAIL = get_config_key(0)
    TWITTER_PASSWORD = get_config_key(1)
    main()
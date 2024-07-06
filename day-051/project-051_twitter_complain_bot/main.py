from selenium import webdriver
from selenium.webdriver.common.by import By
import time


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
        self.__driver.get("https://www.speedtest.net/")

        time.sleep(5)
        accept_button = self.__driver.find_element(By.XPATH, value="/html/body/div[5]/div[2]/div/div/div[2]/div/div/button[2]")
        accept_button.click()

        go_button = self.__driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_button.click()

        time.sleep(60)
        self.up = self.__driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.__driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text

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

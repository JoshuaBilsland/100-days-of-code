from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    # Keep browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("")


if __name__ == "__main__":
    main()

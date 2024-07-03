from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_config_key(line_num):
    try:
        with open('day-049/project-049_linkedin_automation/.config', 'r') as configFile:
            lines = configFile.readlines()
            return lines[line_num].strip()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


def main():
    # Keep browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3946620182&keywords=python%20developer&origin=JOBS_HOME_SEARCH_BUTTON&refresh=true")

    sign_in = driver.find_element(By.CSS_SELECTOR, value="body > div.base-serp-page > header > nav > div > a.nav__button-secondary.btn-md.btn-secondary-emphasis")
    sign_in.click()

    email_entry = driver.find_element(By.ID, value="username")
    password_entry = driver.find_element(By.ID, value="password")
    email = get_config_key(0)
    password = get_config_key(1)
    email_entry.send_keys(email)
    password_entry.send_keys(password, Keys.ENTER)

    input()


if __name__ == "__main__":
    main()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def main():
    # Keep browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://secure-retreat-92358.herokuapp.com/")

    fname = driver.find_element(By.NAME, value="fName")
    lname = driver.find_element(By.NAME, value="lName")
    email = driver.find_element(By.NAME, value="email")

    fname.send_keys("Josh")
    lname.send_keys("Bilsland")
    email.send_keys("an@email.com")

    submit = driver.find_element(By.CSS_SELECTOR, value="form button")
    submit.click()


if __name__ == "__main__":
    main()

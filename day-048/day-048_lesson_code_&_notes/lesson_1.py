from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    # Keep browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.amazon.co.uk/Meta-Quest-128GB-Breakthrough-performance/dp/B0C7VRQ29K")

    # driver.close() = close tab
    # driver.quit() = close browser

    price_pounds = driver.find_element(By.CLASS_NAME, value="a-price-whole")
    price_pence = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
    print(price_pounds.text)
    print(price_pence.text)

    # search_bar = driver.find_element(By.NAME, value="q")
    # button = driver.find_element(By.ID, value="submit")
    # doc_link  = driver.find.element(By.CSS_SELECTOR, value=".documentation-widget a")
    # xpath = driver.find.element(BY.XPATH, value='//*[@id="tabs--1-tab-2"]/span/span[1]')


if __name__ == "__main__":
    main()

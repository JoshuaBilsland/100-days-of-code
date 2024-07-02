import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    # Keep browser open after program finishes
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://orteil.dashnet.org/experiments/cookie/")

    cookie = driver.find_element(By.ID, value="cookie")
    items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    item_ids = [item.get_attribute("id") for item in items]

    start_time = time.time()
    upgrade_check_time = time.time() + 5
    while (time.time() - start_time) < 30:
        cookie.click()

        # Check every 5 seconds for upgrades to buy
        if time.time() > upgrade_check_time:
            all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
            item_prices = []

            for price in all_prices:
                print(price)
                str_price = price.text
                if str_price != "":
                    cost = int(str_price.split("-")[1].strip().replace(",", ""))
                    item_prices.append(cost)

            cookie_upgrades = {}
            for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]] = item_ids[n]

            money_element = driver.find_element(by=By.ID, value="money").text
            if "," in money_element:
                money_element = money_element.replace(",", "")
            cookie_count = int(money_element)

            affordable_upgrades = {}
            for cost, id in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = id

            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element(by=By.ID, value=to_purchase_id).click()
            upgrade_check_time = time.time() + 5
    cookies_per_second = driver.find_element(By.ID, value="cps").text
    print(f"You have achieved {cookies_per_second} cookies per second")


if __name__ == "__main__":
    main()

import requests
import lxml
import smtplib
from bs4 import BeautifulSoup


def get_config_line(line_num):
    try:
        with open('day-047/project-047_price_tracker/.config', 'r') as configFile:
            lines = configFile.readlines()
            return lines[line_num].strip()
    except FileNotFoundError:
        print("ERROR: .config file does not exist.")
        exit()


def main():
    amazon_product_url = "https://www.amazon.co.uk/Meta-Quest-128GB-Breakthrough-performance/dp/B0C7VRQ29K?th=1"
    request_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept_Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    response = requests.get(amazon_product_url, headers=request_headers)

    soup = BeautifulSoup(response.content, "lxml")
    price = soup.find(class_="a-offscreen").get_text()
    price_without_currency = price.split("£")[1]
    price_as_float = float(price_without_currency)

    title = soup.find(id="productTitle").get_text().strip()
    email = get_config_line(0)
    print(email)
    print(type(email))
    app_pw = get_config_line(1)
    BUY_PRICE = 500
    if price_as_float < BUY_PRICE:
        message = f"{title} is now {price}"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            result = connection.login(email, app_pw)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{amazon_product_url}".encode("utf-8")
            )


if __name__ == "__main__":
    main()

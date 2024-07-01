import requests


def main():
    amazon_product_url = "https://www.amazon.co.uk/Meta-Quest-128GB-Breakthrough-performance/dp/B0C7VRQ29K?th=1"
    request_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Accept_Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    amazon_product = requests.get(amazon_product_url, headers=request_headers)
    
    print(amazon_product)


if __name__ == "__main__":
    main()
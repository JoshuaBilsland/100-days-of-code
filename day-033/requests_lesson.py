import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.raise_for_status())
print(response)
data = response.json()
longitude = data["iss_position"]["longitude"]
print(data)
print(longitude)

import requests

url = "https://httpbin.org/get"

response = requests.get(url)

data = response.json()
print(data)
import requests

response = requests.get("https://m.stock.naver.com/")
print(response.text)
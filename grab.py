import requests
from bs4 import BeautifulSoup

name = input("Phone name (like Galaxy Z Fold3): ")
url = f"https://www.sellcell.com/search/?q={name}"
req = requests.get(url).text
doc = BeautifulSoup(req, "html.parser")
price = doc.find(class_="price")
print(price.text)
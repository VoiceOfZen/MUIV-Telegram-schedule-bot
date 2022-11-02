import requests
from requests_html import HTMLSession

url = open("URL", "r")
session = HTMLSession()

data = session.get(url.read()).text

print(data)



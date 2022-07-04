import requests

url = 'http://ale666.narod.ru/foto/1_001.jpg'

res = requests.get(url)
print(res.content)
name = "photos/photo1.jpg"

with open(name, "wb") as file:
    file.write(res.content)


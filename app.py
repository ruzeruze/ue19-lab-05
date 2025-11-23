import requests as req

URL = "https://api.chucknorris.io/jokes/random"

resp = req.get(URL)
resp = resp.json()
print(resp['value'])

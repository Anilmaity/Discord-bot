
import requests


def ltp(currency):
    url = "https://api.coindcx.com/exchange/ticker"
    response = requests.get(url)
    data = response.json()
    for x in range(0, len(data)):
        if data[x]['market'] == str(currency):
            return data[x]["last_price"]
        elif x == len(data)-1:
            return 'Cant find it'


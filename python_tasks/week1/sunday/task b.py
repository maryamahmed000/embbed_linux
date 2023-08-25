import requests


def get_bitcoin_rate():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        rate = data["bpi"]["USD"]["rate"]
        return rate
    except requests.exceptions.RequestException as e:
        print("Error fetching Bitcoin rate:", e)
        return None

# Get the current Bitcoin rate
bitcoin_rate = get_bitcoin_rate()

if bitcoin_rate is not None:
    print("Current Bitcoin rate in USD:", bitcoin_rate)
else:
    print("Unable to fetch Bitcoin rate.")
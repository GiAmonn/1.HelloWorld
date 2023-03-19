import requests
import sys
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    amount = int(input("Amount of Bitcoins: "))
    usd_rate = str((response.json()["bpi"]["USD"]["rate_float"]))
    final_price = float(amount * usd_rate)

    print(f"Current prince of {amount} Bitcoin(s) is {final_price:,.4f}")

except ValueError:
    sys.exit('Command-line argument is not a number')

except IndexError:
    sys.exit('Missing command-line argument')
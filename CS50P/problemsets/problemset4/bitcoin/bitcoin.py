import sys
import json
import requests

# user us command line argument to enter the amount of btc

if len(sys.argv) != 2:
    print("Missing command-line argument")
    sys.exit(1)

# make sure user input can be a float
try:
    btc_amount = float(sys.argv[1])
except ValueError:
    print("Command-line arguement is not a number")
    sys.exit(1)

#request the data from the website through api key
response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=24cf991137c795d514b6c4d4fa38aee7f90474c6cb52f6fd7d710f18fd163925")

# put it in json format
btcdata = response.json()["data"]["priceUsd"]

float(btcdata)

total = btc_amount*btcdata

print(f"${total:,.4f}")








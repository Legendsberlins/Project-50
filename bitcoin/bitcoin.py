import requests
import sys
import json

#Output an error message if cla is not equal to 2
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
#If user inputs number as CLA[1]
try:
    number = float(sys.argv[1])
    #Get coindesk api into the program
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    #View it as json
    json_response = response.json()
    #Generate price of bitcoin of users input (CLA[1]) based on API data
    price = number * json_response["bpi"]["USD"]["rate_float"]
    print(f"${price:,.4f}")

    # print(json.dumps(response.json(), indent = 2)) to arrange the json dicts and lists
#If user does not input number
except ValueError:
    sys.exit("Command-line argument is not a number")
#General request exception
except requests.RequestException:
    sys.exit("Request exception")

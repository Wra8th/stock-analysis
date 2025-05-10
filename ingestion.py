import requests
from dotenv import load_dotenv
import os
import json

def configure():
    load_dotenv()

def alpha_api(symbol, interval):
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={os.getenv('api_key')}"
    r = requests.get(url)
    data = r.json()
    json_data = json.dumps(data, indent=4)
    print(data)
    with open('jsondump1.json', 'w') as file:
        file.write(json_data)
    print('Successfully generated json')

def alpha_api_symbol(keywords):
    # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
    url = f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keywords}&apikey={os.getenv('api_key')}"
    r = requests.get(url)
    data = r.json()
    first_result = data['bestMatches'][0]
    return first_result['1. symbol']

def main():
    configure()
    stock_symbol = alpha_api_symbol('Apple') 
    alpha_api(str(stock_symbol), '1min')
    

main()
import requests
import yaml
import http

from datetime import datetime, timezone, timedelta, date

tz = timezone(timedelta(hours=+8))


with open(r'./config.yaml', 'r') as file:
    config = yaml.full_load(file)
 

class CoinMarketAPI():
    
    APIKey = config['coin_market_cap_api_Key']
    DomainName = "pro-api.coinmarketcap.com"
    symbols = config['symbols']

    @classmethod
    def parse_symbol(cls, symbolList):
        symbols = ''
        for index, symbol in enumerate(symbolList):
            if index == 0:
                symbols += symbol
            else:
                symbols = symbols + ',' + symbol  
        return symbols
    
    @classmethod
    def parse_url(cls, uri:str):
        return f'https://{cls.DomainName}{uri}'

    @classmethod
    def send_request(cls, url, params):
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': cls.APIKey,
        }
        try:
            res = requests.get(url, headers=headers, params=params)
            if res.status_code != http.HTTPStatus.OK:
                print('Error Detail: ', res.json())
            return res
        except Exception as error:
            print(error)
            raise error      
    
    @classmethod
    def get_all_price(cls) -> dict:
        url = cls.parse_url("/v1/cryptocurrency/quotes/latest")
        query_strings = {
            'symbol' : cls.parse_symbol(cls.symbols)
        }
        result = cls.send_request(url=url, params=query_strings)
        
        crypto_price_info = dict()
        try:
            query_results = result.json()['data']
            for symbol in cls.symbols:
                crypto_price_info.update({symbol:query_results[symbol]['quote']['USD']['price']})
            return crypto_price_info
        except Exception as error:
            print(error)
            raise error  
        
    
    @classmethod
    def get_historical_quote(cls, symbol:str) -> dict:
        url = cls.parse_url(f"/v2/cryptocurrency/quotes/historical")
        current_time = date.today()
        end_time = current_time - timedelta(weeks=12)
        query_strings = {
            "symbol": symbol,
            "time_start": current_time.isoformat(),
            "time_end":end_time,
            "count":10,
            "interval":"daily",
        }
        result = cls.send_request(url=url, params=query_strings)
        price_list = []
        try:
            query_results = result.json()['data']
            for quote in query_results["quotes"]:
                price_list.append(quote)
            return price_list
        except Exception as error:
            print(error)
            raise error
        

        
           
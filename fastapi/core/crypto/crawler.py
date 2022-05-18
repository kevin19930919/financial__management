import requests
import json
import yaml


# ==============from config import env============
with open(r'fastapi/core/crypto/config.yaml', 'r') as file:
    config = yaml.full_load(file)

# =========main function==========================
class CoinMarketAPI():
    
    APIKey = config['APIKey']
    DomainName = config['DomainName']
    uri = config['uri']
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
    def send_request(cls, url, headers, params):
        try:
            CryptoPriceInfo = dict()
            res = requests.get(url, headers=headers, params=params)
            queryResults = res.json()['data']
            for symbol in cls.symbols:
                CryptoPriceInfo.update({symbol:queryResults[symbol]['quote']['USD']['price']})
            return CryptoPriceInfo
        except Exception as e:
            print(e)
            raise e      
    
    @classmethod
    def request_price(cls) -> dict:
        url = f'https://{cls.DomainName}{cls.uri}'
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': cls.APIKey,
        }
        queryStrings = {
            'symbol' : cls.parse_symbol(cls.symbols)
        }
        return cls.send_request(url=url, headers=headers, params=queryStrings)
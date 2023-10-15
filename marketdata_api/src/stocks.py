import requests
import pandas as pd
import json

class Stock: 
    def __init__(self, api_key: str, options: dict | None = None):
        self.api_key = api_key
        self.options = options

def get_candles_from_to(self, switch: str,  symbol: str, from_date: str, to_date: str, scale: str):
    """
    :get_candles('s', 'MSFT', '2023-02-03', '2023-02-04', 'D')
    :switch     : 's', stocks | 'i', indices
    :Date Format: ('2023-01-15')
    :Minutely Scale: (minutely, 1, 3, 5, 15, 30, 45, ...)
    :Hourly Scale: (hourly, H, 1H, 2H, ...)
    :Daily Scale: (daily, D, 1D, 2D, ...)
    :Weekly Scale: (weekly, W, 1W, 2W, ...)
    :Monthly Scale: (monthly, M, 1M, 2M, ...)
    :Yearly Scale:(yearly, Y, 1Y, 2Y, ...)
    """

    def url_switch(switch):
        if switch == 's':
            url = 'https://api.marketdata.app/v1/stocks/candles/'
        elif switch == 'i':
            url = 'https://api.marketdata.app/v1/indices/candles/'
        else:
            return "Invalid switch parameter"
        return url

    # https://api.marketdata.app/v1/stocks/candles/D/AAPL?from=2020-01-01&to=2020-12-31

    url = url_switch(switch)

    headers = {'Authorization': self.api_key}

    path = f'{scale}/{symbol}/?from={from_date}&to={to_date}&dateformat=timestamp'

    final_url = url + path
    candles = requests.get(final_url, headers=headers)
    candles = candles.text
    candles_pd = json.loads(candles)
    candles_hist = pd.DataFrame(candles_pd)
    candles_hist['symbol'] = symbol
       
    # rename the columns
    columns = {
        'c': 'close',
        'h': 'high',
        'l': 'low',
        'o': 'open',
        'v': 'volume',
        't': 'date'
    }
    candles_hist.rename(columns=columns, inplace=True)
    candles_hist.drop(['s'], axis=1, inplace=True)
    candles_hist = candles_hist.reindex(columns=['symbol','date', 'close', 'high', 'low', 'open', 'volume'])
    return candles_hist


def get_candles_from(self, switch: str,  symbol: str, from_date: str, scale: str):
    """
    :get_candles('s', 'MSFT', '2023-02-03', 'D')
    :switch     : 's', stocks | 'i', indices
    :Date Format: ('2023-01-15')
    :Minutely Scale: (minutely, 1, 3, 5, 15, 30, 45, ...)
    :Hourly Scale: (hourly, H, 1H, 2H, ...)
    :Daily Scale: (daily, D, 1D, 2D, ...)
    :Weekly Scale: (weekly, W, 1W, 2W, ...)
    :Monthly Scale: (monthly, M, 1M, 2M, ...)
    :Yearly Scale:(yearly, Y, 1Y, 2Y, ...)
    """

    def url_switch(switch):
        if switch == 's':
            url = 'https://api.marketdata.app/v1/stocks/candles/'
        elif switch == 'i':
            url = 'https://api.marketdata.app/v1/indices/candles/'
        else:
            return "Invalid switch parameter"
        return url

    # url = 'https://api.marketdata.app/v1/stocks/candles/'

    url = url_switch(switch)

    # https://api.marketdata.app/v1/stocks/candles/D/AAPL/?from=2023-02-01&dateformat=timestamp  
    
    headers = {'Authorization': self.api_key}

    path = f'{scale}/{symbol}/?from={from_date}&dateformat=timestamp'

    final_url = url + path
    candles = requests.get(final_url, headers=headers)
    candles = candles.text
    candles_pd = json.loads(candles)
    candles_hist = pd.DataFrame(candles_pd)
    candles_hist['symbol'] = symbol
       
    # rename the columns
    columns = {
        'c': 'close',
        'h': 'high',
        'l': 'low',
        'o': 'open',
        'v': 'volume',
        't': 'date'
    }
    candles_hist.rename(columns=columns, inplace=True)
    candles_hist.drop(['s'], axis=1, inplace=True)
    candles_hist = candles_hist.reindex(columns=['symbol','date', 'close', 'high', 'low', 'open', 'volume'])
    return candles_hist


def get_quote_live(self, switch: str,  symbol):
    """
    get_quote_live('s', 'AAPL')

    switch         :'s', stock | 'i', indices
    symbol         :'AAPL'
    """
    def url_switch(switch):
        if switch == 's':
            url = 'https://api.marketdata.app/v1/stocks/quotes/'
        elif switch == 'i':
            url = 'https://api.marketdata.app/v1/indices/quotes/'
        else:
            return "Invalid switch parameter"
        return url



    # https://api.marketdata.app/v1/stocks/quotes/AAPL/?dateformat=timestamp

    url = url_switch(switch)
 
    headers = {'Authorization': self.api_key}
    path = f'{symbol}/?dateformat=timestamp'
    final_url = url + path
    chain_expr = requests.get(final_url, headers=headers)
    
    return chain_expr.text
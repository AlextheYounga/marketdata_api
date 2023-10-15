import requests
import numpy as np
import pandas as pd
import datetime

class Quote():
    def __init__(self, api_key: str, options: dict | None = None):
        self.api_key = api_key
        self.options = options

    def get_historic_quotes_from_to(self, symbol_list: list[str], from_date: str, to_date: str):
        """
        get_historic_quotes_from_to(spx_list, '2023-01-26', '2023-02-04')
        symbol_list      :['SPX230217C04100000','SPX230217P04100000']
        from_date        :'2023-01-26'
        to_date          :'2023-02-04'
        """
        # This function still needs a bit of work.  Getting an error message when going to far out on the term.  thinking it may be that
        # the OptionSymbol is listed, but no quote...  Need to study future...  But Seems to work ok except for those exceptions.

        # https://api.marketdata.app/v1/options/quotes/AAPL250117C00150000/?from=2023-01-01&to=2023-01-31&dateformat=timestamp

        url = 'https://api.marketdata.app/v1/options/quotes/'

        headers = {'Authorization': self.api_key}

        symbols = symbol_list

        # Initialize an empty DataFrame to hold the data
        df = pd.DataFrame()

        # Iterate through the symbols, making a request for each one
        for symbol in symbols:
            # Build the path by concatenating the symbol, date and date_format
            path = f'{symbol}/?from={from_date}&to={to_date}&dateformat=timestamp'
            # Concatenate the base URL and the path
            final_url = url + path
            # Make the request

            response = requests.get(final_url, headers=headers)
            # Extract the data from the response
            data = response.json()

            # Create a new DataFrame with the data and a column for the symbol
            symbol_df = pd.DataFrame({'updated': data.get('updated', np.nan),
                                      'symbol': symbol,
                                      'bid': data.get('bid', np.nan),
                                      'bidSize': data.get('bidSize', np.nan),
                                      'mid': data.get('mid', np.nan),
                                      'ask': data.get('ask', np.nan),
                                      'askSize': data.get('askSize', np.nan),
                                      'last': data.get('last', np.nan),
                                      'openInterest': data.get('openInterest', np.nan),
                                      'volume': data.get('volume', np.nan),
                                      'inTheMoney': data.get('inTheMoney', np.nan),
                                      'intrinsicValue': data.get('intrinsicValue', np.nan),
                                      'extrinsicValue': data.get('extrinsicValue', np.nan),
                                      'underlyingPrice': data.get('underlyingPrice', np.nan)})

            # Add a new column to symbol_df with the id and date values concatenated
            symbol_df['id'] = symbol + '_' + symbol_df['updated'].astype(str)
            # Use the new column as the index when concatenating with df
            df = pd.concat([df, symbol_df.set_index('id')],
                           ignore_index=False, sort=False, axis=0)
        return df

    def get_historic_quotes_from(self, symbol_list: list[str], from_date: str):
        """
        get_historic_quotes_from(spx_list, '2023-01-26')
        symbol_list      :['SPX230217C04100000','SPX230217P04100000']
        from_date        :'2023-01-26'
        """
        # This function still needs a bit of work.  Getting an error message when going to far out on the term.  th
        # the OptionSymbol is listed, but no quote...  Need to study future...  But Seems to work ok except for tho

        # https://api.marketdata.app/v1/options/quotes/AAPL250117C00150000/?from=2023-01-01&to=2023-01-31&dateformat=timestamp

        url = 'https://api.marketdata.app/v1/options/quotes/'

        headers = {'Authorization': self.api_key}

        symbols = symbol_list

        # Initialize an empty DataFrame to hold the data
        df = pd.DataFrame()

        # Iterate through the symbols, making a request for each one
        for symbol in symbols:
            # Build the path by concatenating the symbol, date and date_format
            path = f'{symbol}/?from={from_date}&dateformat=timestamp'
            # Concatenate the base URL and the path
            final_url = url + path
            # Make the request

            response = requests.get(final_url, headers=headers)
            # Extract the data from the response
            data = response.json()

            # Create a new DataFrame with the data and a column for the symbol
            symbol_df = pd.DataFrame({'updated': data.get('updated', np.nan),
                                      'symbol': symbol,
                                      'bid': data.get('bid', np.nan),
                                      'bidSize': data.get('bidSize', np.nan),
                                      'mid': data.get('mid', np.nan),
                                      'ask': data.get('ask', np.nan),
                                      'askSize': data.get('askSize', np.nan),
                                      'last': data.get('last', np.nan),
                                      'openInterest': data.get('openInterest', np.nan),
                                      'volume': data.get('volume', np.nan),
                                      'inTheMoney': data.get('inTheMoney', np.nan),
                                      'intrinsicValue': data.get('intrinsicValue', np.nan),
                                      'extrinsicValue': data.get('extrinsicValue', np.nan),
                                      'underlyingPrice': data.get('underlyingPrice', np.nan)})

            # Add a new column to symbol_df with the id and date values concatenated
            symbol_df['id'] = symbol + '_' + symbol_df['updated'].astype(str)
            # Use the new column as the index when concatenating with df
            df = pd.concat([df, symbol_df.set_index('id')],
                           ignore_index=False, sort=False, axis=0)

        return df

    def get_quote_live(self, symbol: str, expiry_date: str, option_type: str, strike_price: int | float):
        """
        Get Live quotes of an option from a beginning date.
        example       : get_quote_live('IBM', '2023-02-10', 'C', '140')
        symbol        : Symbol of the underlying asset
        expiry_date   : Expiry date of the option in the format 'YYYY-MM-DD'
        option_type   : Option type, either 'C' (Call) or 'P' (Put)
        strike_price  : Strike price of the option    

        Returns:
            JSON response from the API.
        """
        expiry_date = datetime.strptime(expiry_date, '%Y-%m-%d')
        expiry_date = expiry_date.strftime('%y%m%d')
        strike_price = '{:0>8}'.format(int(strike_price) * 1000)
        option_symbol = f'{symbol}{expiry_date}{option_type}{strike_price}'

        url = 'https://api.marketdata.app/v1/options/quotes/'

        headers = {'Authorization': self.api_key}

        path = f'{option_symbol}/?dateformat=timestamp'
        final_url = url + path

        chain_response = requests.get(final_url, headers=headers)
        return chain_response.text


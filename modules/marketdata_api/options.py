import requests
import numpy as np
import pandas as pd

class Option():
    def __init__(self, api_key: str):
        self.api_key = api_key

    def build_symbol(self, symbol: str, expiry_date: str, option_type: str, strike: int | float):
        
        """
        Build an Option Symbol

        example       : build_symbol('IBM', '2023-02-10', 'C', 140)
        symbol        : Symbol of the underlying asset
        expiry_date   : Expiry date of the option in the format 'YYYY-MM-DD'
        option_type   : Option type, either 'C' (Call) or 'P' (Put)
        strike_price  : Strike price of the option, enter as number ('no quotes', ie 100)
                
        """
        # Remove hyphens from the expiry date
        expiry_date = expiry_date.replace('-', '')

        # Format the year as '23'
        year_formatted = expiry_date[2:]

        # Pad the strike price to a 7-digit string with leading zeroes
        # By converting to cents and padding it with a 0
        strike_formatted = f"{int(strike * 100):07d}0"

        option_symbol = f'{symbol}{year_formatted}{option_type[0].upper()}{strike_formatted}'
        return option_symbol

    def get_chain_live(self, symbol: str):
        """
        get_chain_live('AAPL')
        symbol         :'AAPL'
        """
        # https://api.marketdata.app/v1/options/chain/AAPL/?dateformat=timestamp

        url = 'https://api.marketdata.app/v1/options/chain/' 
    
        headers = {'Authorization': self.api_key}
        path = f'{symbol}/?dateformat=timestamp'
        final_url = url + path
        chain_expr = requests.get(final_url, headers=headers)
        
        return chain_expr.text

    def get_chain_from(self, symbol, from_date):
        """
        get_chain_expr('AAPL', '2023-02-17')
        symbol         :'AAPL'
        from_date    :'2023-02-17'
        """

        #https://api.marketdata.app/v1/options/chain/AAPL/?date=2020-01-06&dateformat=timestamp

        url = 'https://api.marketdata.app/v1/options/chain/'
            
        date_format = 'timestamp'
        headers = {'Authorization': self.api_key}
        
        path = f'{symbol}/?date={from_date}&dateformat=timestamp'

        final_url = url + path
        chain_expr = requests.get(final_url, headers=headers)

        return chain_expr.text


    def get_chain_expr(self, symbol, expiry_date):
        """
        Current Option Chains, See
        get_chain_expr_from(symbol, expiry_date, from_date
        for Expr Chains
        get_chain_expr('AAPL', '2023-02-17')
        symbol         :'AAPL'
        expiry_date    :'2023-02-17'
        """

        # https://api.marketdata.app/v1/options/chain/AAPL/?expiration=2024-01-19&dateformat=timestamp

        url = 'https://api.marketdata.app/v1/options/chain/'
            
        date_format = 'timestamp'
        headers = {'Authorization': self.api_key}
        
        path = f'{symbol}/?expiration={expiry_date}&dateformat=timestamp'

        final_url = url + path
        chain_expr = requests.get(final_url, headers=headers)

        return chain_expr.text
        
    def get_chain_expr_from(self, symbol, expiry_date, from_date):
        """
        Expired Option Chains, See
        get_chain_expr(symbol, expiry_date)
        for Current Chains
        get_chain_expr('AAPL', '2023-02-17')
        symbol         :'AAPL'
        expiry_date    :'2023-02-17'
        """

        # https://api.marketdata.app/v1/options/chain/AAPL/?expiration=2024-01-19&dateformat=timestamp  #Current Chains
        # https://api.marketdata.app/v1/options/chain/AAPL/?expiration=2023-03-10&date=2023-03-10&dateformat=timestamp  #Expr Chains

        url = 'https://api.marketdata.app/v1/options/chain/'
            
        headers = {'Authorization': self.api_key}
        
        path = f'{symbol}/?expiration={expiry_date}&date={from_date}&dateformat=timestamp'

        final_url = url + path
        chain_expr = requests.get(final_url, headers=headers)

        return chain_expr.text	
        
        

    def get_chain_weekly(self, symbol):
        """
        get_chain_weekly('SPX')
        symbol:     :'SPX'

        """
        # https://api.marketdata.app/v1/options/chain/AAPL/?monthly=false&dateformat=timestamp
        
        url = 'https://api.marketdata.app/v1/options/chain/'  #AAPL/?monthly=true&dateformat=timestamp
        
        
        headers = {'Authorization': self.api_key}

        path = f'{symbol}/?monthly=false&dateformat=timestamp'

        final_url = url + path
        chain_expr = requests.get(final_url, headers=headers)
        return chain_expr.text

    def get_chain_monthly(self, symbol):
        """
        get_chain_monthly('SPX')
        symbol:     :'SPX'
        """
        # https://api.marketdata.app/v1/options/chain/AAPL/?monthly=true&dateformat=timestamp
        
        url = 'https://api.marketdata.app/v1/options/chain/'  #AAPL/?monthly=true&dateformat=timestam
        
        
        headers = {'Authorization': self.api_key}

        path = f'{symbol}/?monthly=true&dateformat=timestamp'

        final_url = url + path
        chain_expr = requests.get(final_url, headers=headers)
        return chain_expr.text

    def get_chain_year(self, symbol, year):
        """
        get_chain_year('IBM', '2022')
        symbol      :'IBM'
        year        :'2023'
        """
        # https://api.marketdata.app/v1/options/chain/AAPL/?year=2022&dateformat=timestamp
        
        url = 'https://api.marketdata.app/v1/options/chain/'  #AAPL/?monthly=true&dateformat=timestamp    
        
        headers = {'Authorization': self.api_key}

        path = f'{symbol}/?year={year}&dateformat=timestamp'

        final_url = url + path
        chain_expr = requests.get(final_url, headers=headers)
        return chain_expr.text

    def get_chain_strike(self, symbol, strike):
        """
        get_chain_strike('IBM', '150')
        symbol      :'IBM'
        strike      :'150'
        """
        # https://api.marketdata.app/v1/options/chain/AAPL/?strike=150&dateformat=timestamp
        
        url = 'https://api.marketdata.app/v1/options/chain/'  #AAPL/?monthly=true&dateformat=timest
            
        headers = {'Authorization': self.api_key}

        path = f'{symbol}/?strike={strike}&dateformat=timestamp'

        final_url = url + path
        chain_expr = requests.get(final_url, headers=headers)
        return chain_expr.text

    def get_historic_quotes_from_to(self, symbol_list, from_date, to_date):
        """
        get_chain_strike(spx_list, '2023-01-26', '2023-02-04')
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
                            'ask': data.get('ask',np.nan),
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
            df = pd.concat([df, symbol_df.set_index('id')], ignore_index=False, sort=False, axis=0)
        return df

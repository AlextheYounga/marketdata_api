import requests

class Chain():
    def __init__(self, api_key: str, options: dict | None = None):
        """
        Initialize the Chain class with your API key and optional options
        See docs for more info on options
        options: {
            'output': 'json' | 'txt' | 'pd' | 'debug'    => default: 'json'
            'map': True | False
        }
        """
        self.api_key = api_key
        self.options = options

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
        
        return chain_expr

    def get_chain_from(self, symbol: str, from_date: str):
        """
        get_chain_expr('AAPL', '2023-02-17')
        symbol         :'AAPL'
        from_date    :'2023-02-17'
        """

        #https://api.marketdata.app/v1/options/chain/AAPL/?date=2020-01-06&dateformat=timestamp

        url = 'https://api.marketdata.app/v1/options/chain/'
            
        headers = {'Authorization': self.api_key}
        
        path = f'{symbol}/?date={from_date}&dateformat=timestamp'

        final_url = url + path
        chain_expr = requests.get(final_url, headers=headers)

        return chain_expr


    def get_chain_expr(self, symbol: str, expiry_date: str):
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
            
        headers = {'Authorization': self.api_key}
        
        path = f'{symbol}/?expiration={expiry_date}&dateformat=timestamp'

        final_url = url + path
        chain_expr = requests.get(final_url, headers=headers)

        return chain_expr
        
    def get_chain_expr_from(self, symbol: str, expiry_date: str, from_date: str):
        """
        Expired Option Chains, See
        get_chain_expr(symbol, expiry_date)
        for Current Chains
        get_chain_expr('AAPL', '2023-02-17')
        symbol         :'AAPL'
        expiry_date    :'2023-02-17'
        from_date      :'2023-01-26'
        """

        # https://api.marketdata.app/v1/options/chain/AAPL/?expiration=2024-01-19&dateformat=timestamp  #Current Chains
        # https://api.marketdata.app/v1/options/chain/AAPL/?expiration=2023-03-10&date=2023-03-10&dateformat=timestamp  #Expr Chains

        url = 'https://api.marketdata.app/v1/options/chain/'
            
        headers = {'Authorization': self.api_key}
        
        path = f'{symbol}/?expiration={expiry_date}&date={from_date}&dateformat=timestamp'

        final_url = url + path
        chain_expr = requests.get(final_url, headers=headers)

        return chain_expr	
        
        

    def get_chain_weekly(self, symbol: str):
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
        return chain_expr

    def get_chain_monthly(self, symbol: str):
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
        return chain_expr

    def get_chain_year(self, symbol: str, year: str):
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
        return chain_expr

    def get_chain_strike(self, symbol: str, strike: str):
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
        return chain_expr


    def _format_output(self, response):
        """
        Format the output of the API call based on the options passed in
        """
        format = self.options['format']
        if format == 'json':
            return response.json()
        elif format == 'txt':
            return response.text
        elif format == 'pd':
            pass
            # return response
        elif format == 'debug':
            return response
        else:
            return response.json()
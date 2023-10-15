import os
from dotenv import load_dotenv
from marketdata_api.src.options.chain import Chain
import json
load_dotenv()

api_key = os.environ.get("API_KEY")
api = Chain(api_key)
chain = api.get_chain_live("AAPL")

with open('storage/chain.json', 'w') as outfile:
    json.dump(chain, outfile)
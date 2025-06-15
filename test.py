import json
import pandas as pd
import yfinance as yf

# json_data = pd.read_json('./jsondump1.json')

# df = json_data['Time Series (1min)']

# print("this is dataframe")
# print(df['2025-06-06 14:54:00'])

#print(dir(yf))
# ['AsyncWebSocket', 'EquityQuery', 'FundQuery', 'Industry', 'Lookup', 'Market', 'PREDEFINED_SCREENER_QUERIES', 'Search', 'Sector', 'Ticker', 'Tickers', 'WebSocket', 'YfData', '_NOTSET', '__all__', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'base', 'cache', 'const', 'data', 'domain', 'download', 'enable_debug_mode', 'exceptions', 'live', 'lookup', 'multi', 'pricing_pb2', 'scrapers', 'screen', 'screener', 'search', 'set_config', 'set_tz_cache_location', 'shared', 'ticker', 'tickers', 'utils', 'version', 'warnings']

data = yf.download("INTC", period='1y', interval='1d')
print(data.columns)
print(data['Close'])
data.to_csv('./data.csv')  
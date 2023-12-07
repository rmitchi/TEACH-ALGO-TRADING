import io
import requests
import pandas as pd
import yfinance as yf

symbol = input("Enter symbol: ")

# Get LTP
df = yf.download(f"{symbol}.NS", interval='1m', period="1d", progress=False)
ltp = df['Close'].iat[-1]
print(ltp)

# Download options chain
def get_options_chain(symbol: str) -> dict:
	"""
	"""
	txt = requests.get(url="https://api.kite.trade/instruments", verify=True).content
	zerodha_token_list = pd.read_csv(io.StringIO(txt.decode('utf-8')))
	zerodha_token_list.rename(columns={"instrument_token": "brokerToken", "exchange_token": "exchangeToken", "tradingsymbol": "symbol"}, inplace=True)
	zerodha_token_list['expiry'] = pd.to_datetime(zerodha_token_list['expiry'], format="%Y-%m-%d")
	zerodha_token_list['liveFeedToken'] = zerodha_token_list['exchangeToken']
	zerodha_token_list['brokerToken'] = zerodha_token_list['exchangeToken']
	zerodha_token_list = zerodha_token_list[(zerodha_token_list['instrument_type'] == "CE") | (zerodha_token_list['instrument_type'] == "PE")]
	zerodha_token_list = zerodha_token_list[(zerodha_token_list['exchange'] == "NFO")]

	chain_df = zerodha_token_list[zerodha_token_list['name'] == symbol]
	return chain_df

chain_df = get_options_chain(symbol)
# print(chain_df)

x1 = (ltp // 50) * 50
x2 = x1 + 50
atm_strike = x1 if (abs(ltp - x1) < abs(ltp - x2) ) else x2
# print(atm_strike)

atm_strike_info = chain_df[chain_df['strike'] == atm_strike]

expiries = sorted(atm_strike_info['expiry'].unique())

print("Available expiries: ")
for idx, i in enumerate(expiries):
	print(f"[{idx+1}]: {i.date()}")

selected_exp = input("Select expiry: ")

exp = expiries[int(selected_exp) - 1]

atm_strike_info = atm_strike_info[atm_strike_info['expiry'] == exp]
print(atm_strike_info)

# CALL or PUT
print("[1] CALL")
print("[2] PUT")
ce_pe = input("CALL or PUT: ")
ce_pe = "CE" if ce_pe == "1" else "PE"
atm_strike_info = atm_strike_info[atm_strike_info['instrument_type'] == ce_pe]
print(atm_strike_info)

# Ask buy or sell
print("[1] BUY")
print("[2] SELL")
input("BUY or SELL: ")

# Send buy order
API_KEY = "SaLc4U2fMKWWoKpVINmykpRtE4mT74pR"
API_SECRET = " h7LwODXWyBBAMVJAsumlwT0PFhyE1dbb"

from SharekhanApi.sharekhanConnect import SharekhanConnect

login = SharekhanConnect(API_KEY)
vendor_key = "" 
version_id = "Version Id"
#	"""Only null/1005/1006 version id is allowed to be passed"""
state=12345
url = login.login_url(vendor_key=vendor_key, version_id=version_id)
"""This will provide you the redirect login url which can be used to login in the sharekhan account"""
print(url)

request_token = input("RED: ")

# request_token = "Valid Request Token Value"

"""Use generate session method when you are passing version id """
session=login.generate_session(request_token,API_SECRET)
# Generating access token for version id and pass parameters as it is passed below 
access_token=login.get_access_token(API_KEY,session,state,versionId=version_id)

"""Use generate session without version id method when you are not passing version id """
sessionwithoutvesionId=login.generate_session_without_versionId(request_token,API_SECRET)
# Generating access token for without version id 
access_token=login.get_access_token(API_KEY,sessionwithoutvesionId,state)

print(access_token)

# Make a object for SharekhanConnect class
"""Here we are passing the api-key, access-token and vendor-key(when needed) as a request header parameters"""
access_token = "Your access token value"
sharekhan = SharekhanConnect(API_KEY,access_token)
print(sharekhan.requestHeaders())       # 
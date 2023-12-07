# Send buy order
API_KEY = "SaLc4U2fMKWWoKpVINmykpRtE4mT74pR"
API_SECRET = "h7LwODXWyBBAMVJAsumlwT0PFhyE1dbb"

from SharekhanApi.sharekhanConnect import SharekhanConnect

login = SharekhanConnect(API_KEY)
vendor_key = "" 
version_id = "1005"
#	"""Only null/1005/1006 version id is allowed to be passed"""
state=12345
url = login.login_url(vendor_key=vendor_key, version_id=version_id)
"""This will provide you the redirect login url which can be used to login in the sharekhan account"""
print(url)

# request_token = input("REQUEST TOKEN: ")
# request_token = "4ilPsoAqzM7uEWTXPSyrU2oVFSFVJ23ifQWlpbZ22_RPQodtW2V9qlyostmHF6uFmHm2NcBCK-M="

"""Use generate session method when you are passing version id """
# session=login.generate_session(request_token,API_SECRET)
# # Generating access token for version id and pass parameters as it is passed below 
# access_token=login.get_access_token(API_KEY,session,state,versionId=version_id)
# print("Access token ......")
# {'status': 200, 'message': 'access_token', 'timestamp': '2023-12-07T12:14:30+05:30', 'data': {'customerId': '2396042', 'loginId': 'PARTHMAKWANA', 'token': 'eyJ0eXAiOiJzZWMiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2aEZDM3lydVRYRjlXK3B2bEVmMkZjMmpjdlpHL3Bha010QTQzUkRtWkpxaTA3ZWsyeDJlN29qclBRWXh6TGEySDlxdGNhckRGUW5vcWlSWVRoUzRRbEVDT1BUeUpPLysyaGp5bnJpT0JhdjVBZVI4YXdvZ1grVmVRMWZUSDNVU0lSZ21tWG9lN1psU1YrZ1g3NTRXajhJVXNtQ3V3S1dWNU5hVHVrbUxRRGM9IiwiaWF0IjoxNzAxOTMxNDcwLCJleHAiOjE3MDE5NzM3OTl9.ckiqRP8VxbkdI5MrGZXPanrXHQ62iEHo6sclzsmn3Zk', 'userId': None, 'btplusServiceEnabled': False, 'exchanges': ['NF', 'RN', 'MX', 'BC', 'NC'], 'broker': 'Sharekhan', 'state': '12345', 'fullName': 'PARTH RAJKUMAR MAKWANA'}}
# print(access_token)
access_token = "eyJ0eXAiOiJzZWMiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2aEZDM3lydVRYRjlXK3B2bEVmMkZjMmpjdlpHL3Bha010QTQzUkRtWkpxaTA3ZWsyeDJlN29qclBRWXh6TGEySDlxdGNhckRGUW5vcWlSWVRoUzRRbEVDT1BUeUpPLysyaGp5bnJpT0JhdjVBZVI4YXdvZ1grVmVRMWZUSDNVU0lSZ21tWG9lN1psU1YrZ1g3NTRXajhJVXNtQ3V3S1dWNU5hVHVrbUxRRGM9IiwiaWF0IjoxNzAxOTMxNDcwLCJleHAiOjE3MDE5NzM3OTl9.ckiqRP8VxbkdI5MrGZXPanrXHQ62iEHo6sclzsmn3Zk"
"""Use generate session without version id method when you are not passing version id """
# sessionwithoutvesionId=login.generate_session_without_versionId(request_token,API_SECRET)
# # Generating access token for without version id 
# access_token=login.get_access_token(API_KEY,sessionwithoutvesionId,state)

# print(access_token)

# Make a object for SharekhanConnect class
"""Here we are passing the api-key, access-token and vendor-key(when needed) as a request header parameters"""
sharekhan = SharekhanConnect(API_KEY,state=12345, access_token=access_token)
print(sharekhan.requestHeaders())       # 
# {'api-key': 'SaLc4U2fMKWWoKpVINmykpRtE4mT74pR', 'access-token': {'status': 200, 'message': 'access_token', 'timestamp': '2023-12-07T12:14:30+05:30', 'data': {'customerId': '2396042', 'loginId': 'PARTHMAKWANA', 'token': 'eyJ0eXAiOiJzZWMiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2aEZDM3lydVRYRjlXK3B2bEVmMkZjMmpjdlpHL3Bha010QTQzUkRtWkpxaTA3ZWsyeDJlN29qclBRWXh6TGEySDlxdGNhckRGUW5vcWlSWVRoUzRRbEVDT1BUeUpPLysyaGp5bnJpT0JhdjVBZVI4YXdvZ1grVmVRMWZUSDNVU0lSZ21tWG9lN1psU1YrZ1g3NTRXajhJVXNtQ3V3S1dWNU5hVHVrbUxRRGM9IiwiaWF0IjoxNzAxOTMxNDcwLCJleHAiOjE3MDE5NzM3OTl9.ckiqRP8VxbkdI5MrGZXPanrXHQ62iEHo6sclzsmn3Zk', 'userId': None, 'btplusServiceEnabled': False, 'exchanges': ['NF', 'RN', 'MX', 'BC', 'NC'], 'broker': 'Sharekhan', 'state': '12345', 'fullName': 'PARTH RAJKUMAR MAKWANA'}}, 'Content-type': 'application/json'}

# sharekhan.access_token = access_token

# print(sharekhan.userId)
orderparams={
     "customerId": 2396042,
     "scripCode": 500570,
     "tradingSymbol": "TATAMOTORS",
     "exchange": "BC",
     "transactionType": "B",  #  --> (B, S, BM, SM, SAM)
     "quantity": 1,
     "disclosedQty": 0,
     "price": "0",
     "triggerPrice": "0",
     "rmsCode": "ANY",
     "afterHour": "N",
     "orderType": "NORMAL",
     "channelUser": "parthmakwana",   #   (Use LoginId as ChannelUser)
     "validity": "GFD",#
     "requestType": "NEW",
     "productType": "INV" , #  --> (INVESTMENT or (INV), BIGTRADE or (BT), BIGTRADEPLUS or (BT+))
     #Below parameters need to be added for FNO trading
    # "instrumentType": "OS",   # --> (Future Stocks(FS)/ Future Index(FI)/ Option Index(OI)/ Option Stocks(OS)/ Future Currency(FUTCUR)/ Option Currency(OPTCUR))
    # "strikePrice": "-1",
    # "optionType": "XX",   # --> (XX/PE/CE)
    # "expiry": "31/03/2023"
}

order=sharekhan.placeOrder(orderparams)
print("PlaceOrder: {}".format(order))
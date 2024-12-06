from urllib.parse import parse_qs, urlparse

import pyotp
import requests
from kiteconnect import KiteConnect

api_key = ""
user_id = ""
user_password = ""
totp_key = ""


kite = KiteConnect(api_key=api_key)

session = requests.Session()
response = session.get(kite.login_url())

# User login POST request
login_payload = {
    "user_id": user_id,
    "password": user_password,
}
login_response = session.post("https://kite.zerodha.com/api/login", login_payload)

# TOTP POST request
totp_payload = {
    "user_id": user_id,
    "request_id": login_response.json()["data"]["request_id"],
    "twofa_value": pyotp.TOTP(totp_key).now(),
    "twofa_type": "totp",
    "skip_session": True,
}
totp_response = session.post("https://kite.zerodha.com/api/twofa", totp_payload)

# Extract request token from redirect URL
try:
    response = session.get(kite.login_url())
    parse_result = urlparse(response.url)
    query_parms = parse_qs(parse_result.query)
except Exception as e:
    e1 = str(e)
    e2 = str(e1).split("request_token=",1)[1]
    e2 = e2[:32]

print("Request Token : " + e2)


# save request token key as text file

file1 = open("Data\\request_session.txt","w")   #write mode
file1.write(str(e2))
file1.close()

from kiteconnect import KiteConnect

#get request token from file in automate request token

request_token = "
api_secret = "

kite = KiteConnect(api_key=api_key)

a = kite.generate_session(request_token,api_secret)

api_session = a['access_token']

print(api_session)

# save session key as text file

file1 = open("Data\\api_session.txt","w")   #write mode
file1.write(api_session)
file1.close()

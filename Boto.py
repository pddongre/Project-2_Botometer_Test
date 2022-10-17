import botometer

# with open("CK.txt") as f:
#    consumer_key = f.read()

# with open("CS.txt") as f:
#    consumer_secret = f.read()

# with open("AT.txt") as f:
#    access_token = f.read()

# with open("ATS.txt") as f:
#    access_token_secret = f.read()

rapidapi_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
twitter_app_auth = {
    'consumer_key': 'xxxxxxxx',
    'consumer_secret': 'xxxxxxxxxx',
    'access_token': 'xxxxxxxxx',
    'access_token_secret': 'xxxxxxxxxxx',
  }
  
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)

# Check a single account by screen name
result = bom.check_account('@clayadavis')

# Check a single account by id
result = bom.check_account(1548959833)

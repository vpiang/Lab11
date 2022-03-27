import requests
import json
from getpass import getpass
from requests.auth import HTTPBasicAuth

username = input("please type your username: ")
password = getpass("please enter your password: ")

url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

payload={}
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/json',
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.request("POST", url, headers=headers, data=payload)

tokenJSON = response.json()

TOKEN = tokenJSON['Token']

print('Your token was successfully generated. The value of your token is:\n' + TOKEN)

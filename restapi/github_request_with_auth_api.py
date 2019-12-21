import requests
from pprint import pprint
from requests.auth import HTTPBasicAuth
from getpass import getpass

from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


if __name__ == "__main__":

    username = "k19ran"
    password = getpass()
    url = "https://api.github.com/user"
    #http_headers = {"accept":"application/vnd.github.v3+json"}
    #response = requests.get(url,headers=http_headers,auth=(username,password),verify=False)
    response = requests.get(url,auth=(username,password))
    response = response.json()

print()
print(response)
print()

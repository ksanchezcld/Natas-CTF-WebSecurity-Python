#The password for natas10 :: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

import requests

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

siteUrl = 'http://{username}.natas.labs.overthewire.org'.format(username)

def loginWebSite():
    r = requests.get(siteUrl, auth = (username, password))
    print(r.text)


loginWebSite()
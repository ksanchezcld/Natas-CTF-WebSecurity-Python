#!/usr/bin/env python
#<!--The password for natas1 is gtVrDuiDfck831PqWsLEZy5gyDz1clto -->

import requests
import re

username = 'natas0'
password = username

siteUrl = 'http://{}.natas.labs.overthewire.org'.format(username)

def getAuth401Sample():
    r = requests.get(siteUrl)
    print(r)

def getWebSourceCode():
    r = requests.get(siteUrl, auth = (username, password))
    content = r.text
    print (re.findall('<!--The password for natas1 is (.*) -->', content))

def loginNextChallenge():
    username = 'natas1'
    password = 'gtVrDuiDfck831PqWsLEZy5gyDz1clto'
    challengeUrl = 'http://natas1.natas.labs.overthewire.org' 

    r = requests.get(challengeUrl, auth = (username, password))
    content = r.text
    print(content)


#getAuth401Sample()
#getWebSourceCode()
loginNextChallenge()
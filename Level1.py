#!/usr/bin/env python
#<!--The password for natas2 is ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi -->

import requests
import re

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

siteUrl = 'http://{}.natas.labs.overthewire.org'.format(username)
print(siteUrl)

def loginWebSite():
    r = requests.get(siteUrl, auth = (username, password))
    content = r.text
    print(content)

def loginNextChallenge():
    nextUrl = 'http://{}.natas.labs.overthewire.org'.format(username)
    r = requests.get(nextUrl, auth = (username, password))
    content = r.text
    print(content)

#loginWebSite()
loginNextChallenge()
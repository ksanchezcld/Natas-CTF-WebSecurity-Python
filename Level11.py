#/etc/natas_webpass/natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

import requests
import re
import urllib
import base64

username = 'natas11'
password = 'U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'
siteUrl = 'http://{}.natas.labs.overthewire.org/index-source.html'.format(username)

def loginWebSite():
    r = requests.get(siteUrl, auth = (username, password))
    print(r.text)


def extractCode():
    siteUrl = 'http://{}.natas.labs.overthewire.org'.format(username)
    session = requests.Session()
    r = session.get(siteUrl, auth = (username, password))

    #content = r.text

    print(base64.b64decode(urllib.parse.unquote(session.cookies['data'])))

#loginWebSite()
extractCode()
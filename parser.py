import requests
import json

has_next_key = False
nextKey = ""
page0 = 1
page = 1
sas = "?sv="

def doit(page):
    
    rq = requests.get(baseURL + str(page),headers=hd)
    data = json.loads(rq.content)
    urlist = data['url_list']
    print(page)
    
    for item in urlist:
        svurl = item['url']
        if sas in svurl:
            print(item['url'])
        else:
            ()

baseURL = "https://otx.alienvault.com/api/v1/indicators/domain/windows.net/url_list?limit=500&page="

#/api/v1/pulses/subscribed?page=1 -H 
hd = { 'X-OTX-API-KEY' : 'INSERT API KEY'}

rq = requests.get(baseURL + str(page0),headers=hd)

data = json.loads(rq.content)
urlist = data['url_list']
for item in urlist:
    svurl = item['url']
    if sas in svurl:
        print(item['url'])
    else:
        ()

while data['has_next'] == True:
    page+=1
    doit(page)
    
else:
    ()

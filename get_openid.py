import requests
import json
import sys
import urllib2
def get(code):
        url =  'https://api.weixin.qq.com/sns/jscode2session?appid=wx55cd821ce62b1027&secret=b9707311046d22eb4435022b6a8ca044&js_code=' +code+'&grant_type=authorization_code'
    headers = {'Content-Type':'application/json'}  
    request = urllib2.Request(url)
    request.get_method = lambda : "GET"
    response = urllib2.urlopen(request)
    #print (json.loads(response.read()))
    return (json.loads(response.read()))
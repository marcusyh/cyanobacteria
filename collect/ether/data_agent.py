import urllib2
import json

def data_agent(url):
    src = urllib2.urlopen(url)
    dt  = src.read()
    src.close()

    return json.loads(dt)

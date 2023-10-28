#!/usr/bin/python

import json
import os
import math
from dotenv import load_dotenv
from datetime import datetime, timedelta
#from tzlocal import get_localzone
import requests
load_dotenv()

DAYS = timedelta(90)
#local_tz = get_localzone()
now = datetime.now()
#days_ago = local_tz.normalize(now - DAYS)
#print(days_ago)
naive = now.replace(tzinfo=None) - DAYS
days_ago_ms = naive.timestamp() * 1000
#print(days_ago_ms)
days_ago_final = math.floor(days_ago_ms)
#print(days_ago_final)

room_id = '!OGEhHVWSdvArJzumhm:matrix.org'
data = {}
purge_room_api_url = 'http://localhost:8008/_synapse/admin/v1/rooms'
req_headers = {"Authorization":header_token, "Content-type":"application/json"}

url = "%s/%s" % (purge_room_api_url,room_id)
response = requests.delete(url,headers=req_headers,json=data)
json_response = json.loads(response.text)
print(json_response)
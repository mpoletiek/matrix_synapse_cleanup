#!/usr/bin/python3
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
now_naive = now.replace(tzinfo=None)
now_ms = now_naive.timestamp() * 1000
#print(days_ago_ms)
days_ago_final = math.floor(days_ago_ms)
now_final = math.floor(now_ms)
#print(days_ago_final)

api_token = os.environ.get("API_TOKEN")
print("API TOKEN: %s" % (api_token))

media_api_url = "http://localhost:8008/_synapse/admin/v1/media/delete?before_ts=%s" % (days_ago_final)
print(media_api_url)
header_token = "Bearer %s" % (api_token)
req_headers = {"Authorization":"Bearer %s" % (api_token), "Content-type":"application/json"}
data = {}

response = requests.post(media_api_url, headers=req_headers, json=data)
print(response.text)

### PURGE ALL REMOTE MEDIA
print(now_ms)
remote_media_api_url = "http://localhost:8008/_synapse/admin/v1/purge_media_cache?before_ts=%s" % (now_final)

response = requests.post(remote_media_api_url, headers=req_headers, json=data)
print(response.text)
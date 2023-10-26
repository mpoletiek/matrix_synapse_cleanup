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
#print(days_ago_ms)
days_ago_final = math.floor(days_ago_ms)
#print(days_ago_final)

api_token = os.environ.get("API_TOKEN")
print("API TOKEN: %s" % (api_token))
rooms_api_url = 'http://localhost:8008/_synapse/admin/v1/rooms'
header_token = "Bearer %s" % (api_token)
req_headers = {"Authorization":"Bearer %s" % (api_token), "Content-type":"application/json"}

print("Getting Rooms")
def get_rooms(api_url):
        print("get_rooms")
        response = requests.get(api_url, headers=req_headers)
        #print("response: %s" % (response))
        json_response = json.loads(response.text)
        #print("json response:")
        #print(json_response)

        return json_response

response = get_rooms(rooms_api_url)

for room in response['rooms']:
    print(room['room_id'])

    # foreach room, purge history
    purge_url = "http://localhost:8008/_synapse/admin/v1/purge_history/%s" % (room['room_id'])
    data = {"purge_up_to_ts": days_ago_final}
    response = requests.post(purge_url, headers=req_headers, json=data)
    print(response.text)


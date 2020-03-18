#!/bin/python

import json

# example dictionary that contains data like you want to have in json
details = {
  "slack_config": {
    "slack_username": "SLACK_USERNAME",
    "slack_secret": "SLACK_SECRET",
    "slack_client_id": "SLACK_CLIENT_ID",
    "slack_api_tokent": "SLACK_API_TOKEN"
  },
  "slack_destination": {
    "channel": "SLACK_CHANNEL"
  },
  "slack_message": {
    "message": "INSERT_A_MESSAGE"
  }
}

with open('secrets.json', 'w') as json_file:
    json.dump(details, json_file, indent=4)

# get json string from that dictionary
json = json.dumps(details, indent=4)
print("JSON will be STD.OUT to secrets.json")
print("Please check the current working directory for the file.")
print json

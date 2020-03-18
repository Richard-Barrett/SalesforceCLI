# Integration with Slack 
In order to integrate with Slack you will need to generate a JSON payload in order to send particular messages to your desired channel destination. 

**secrets.json**
```json
{
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
```

What this does is it stores all of the informatin needed to autheticate with Slack, establish a session, and target a desired set of channels. 
Furthermore, it allows you to customize the message you want to send. 
After you have successfully published a message to a hannel you can scheudle it with **Task-Scheduler** or make a **Cronjob**.
You can make a **secrets.json** by using the following command to generate a template within the current working directory. 
```python
python secrets_json_slack_int_maker.py
```

**Before The Script is Ran:**
```bash
.
├── README.md
├── secrets_json_slack_int_maker.py
└── send_message.py
```

**Output:**
```bash
 richardbarret@1152-MacBook-Pro  ~/Git/SalesforceCLI/Integration/Slack   master  python secrets_json_slack_int_maker.py                                 ✔  1054  13:24:56
JSON will be STD.OUT to secrets.json
Please check the current working directory for the file.
{
    "slack_config": {
        "slack_client_id": "SLACK_CLIENT_ID",
        "slack_api_tokent": "SLACK_API_TOKEN",
        "slack_username": "SLACK_USERNAME",
        "slack_secret": "SLACK_SECRET"
    },
    "slack_destination": {
        "channel": "SLACK_CHANNEL"
    },
    "slack_message": {
        "message": "INSERT_A_MESSAGE"
    }
}
```

**After The Script is Ran:**
```bash
.
├── README.md
├── secrets.json
├── secrets_json_slack_int_maker.py
└── send_message.py
```

#!/bin/bash
# ===========================================================
# Created By: Richard Barrett
# Organization: Mirantis
# Department: Customer Success Operation
# Purpose: Send Message to Slack Channel
# Date: 03/20/2020
# ===========================================================

# System Variables
webhook_url="$(jq --raw-output .slack_config.slack_target_url secrets.json)"

# Use Messages in this command syntax
# curl -X POST -H 'Content-type: application/json' --data '{"text":"BODY"}' <insert_URL>
# curl -X POST -H 'Content-type: application/json' --data '{"text":"BODY"}' && echo '{"slack_config": {"slack_target_url": "URL"}}' | jq --raw-output .slack_config.slack_target_url

# Generalt Message:
curl -X POST -H 'Content-type: application/json' --data '{"text":"Please see the following links for Handovers and Change Requests that may impact your shift."}' && echo '{"slack_config": {"slack_target_url": "URL"}}' | jq --raw-output .slack_config.slack_target_url

# Messages for Handover:
curl -X POST -H 'Content-type: application/json' --data '{"text":"Handovers: https://mirantis.my.salesforce.com/00O2S000003g25h"}' && echo '{"slack_config": {"slack_target_url": "URL"}}' | jq --raw-output .slack_config.slack_target_url

# Message for All Change Requests:
curl -X POST -H 'Content-type: application/json' --data '{"text":"All Change Requests: https://mirantis.my.salesforce.com/00O2S000004INH1"}' && echo '{"slack_config": {"slack_target_url": "URL"}}' | jq --raw-output .slack_config.slack_target_url

# Message for Change Requests in Ready to Execute
# curl -X POST -H 'Content-type: application/json' --data '{"text":"All CRs in Ready to Execute:"}' <insert_URL>

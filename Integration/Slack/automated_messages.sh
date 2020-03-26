#!/bin/bash
# ===========================================================
# Created By: Richard Barrett
# Organization: Mirantis
# Department: Customer Success Operation
# Purpose: Send Message to Slack Channel
# Date: 03/20/2020
# ===========================================================

# System Variables
webhook_url=$(cat secrets.json | jq ".slack_config.slack_target_url" | tr -d \")

# Use Messages in this command syntax
# curl -X POST -H 'Content-type: application/json' --data '{"text":"MESSAGE TO INSERT"}' $webhook_url

# Generalt Message:
curl -X POST -H 'Content-type: application/json' --data '{"text":"Please see the following links for Handovers and Change Requests that may impact your shift."}' $webhook_url

# Messages for Handover:
curl -X POST -H 'Content-type: application/json' --data '{"text":"Handovers: https://mirantis.my.salesforce.com/00O2S000003g25h"}' $webhook_url

# Message for All Change Requests:
curl -X POST -H 'Content-type: application/json' --data '{"text":"All Change Requests: https://mirantis.my.salesforce.com/00O2S000004INH1"}' $webhook_url

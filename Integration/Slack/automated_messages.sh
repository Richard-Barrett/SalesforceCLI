#!/bin/bash
# ===========================================================
# Created By: Richard Barrett
# Organization: Mirantis
# Department: Customer Success Operation
# Purpose: Send Message to Slack Channel
# Date: 03/20/2020
# ===========================================================
# Use Messages in this command syntax
# curl -X POST -H 'Content-type: application/json' --data '{"text":"BODY"}' <insert_URL>

# Generalt Message:
curl -X POST -H 'Content-type: application/json' --data '{"text":"Please see the following links for Handovers and Change Requests that may impact your shift."}' https://hooks.slack.com/services/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

# Messages for Handover:
curl -X POST -H 'Content-type: application/json' --data '{"text":"Handovers: https://mirantis.my.salesforce.com/00O2S000003g25h"}' <insert_URL>

# Message for All Change Requests:
curl -X POST -H 'Content-type: application/json' --data '{"text":"All Change Requests: https://mirantis.my.salesforce.com/00O2S000004INH1"}' <insert_URL>

# Message for Change Requests in Ready to Execute
# curl -X POST -H 'Content-type: application/json' --data '{"text":"All CRs in Ready to Execute:"}' <insert_URL>

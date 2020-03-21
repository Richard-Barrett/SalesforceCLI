#!/bin/bash
# ===========================================================
# Created By: Richard Barrett
# Organization: Mirantis
# Department: Customer Success Operation
# Purpose: Send Message to Slack Channel
# Date: 03/20/2020
# ===========================================================
# Use Messages in this command syntax
# curl -X POST -H 'Content-type: application/json' --data '{"text":"BODY"}' https://hooks.slack.com/services/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

# Generalt Message:
curl -X POST -H 'Content-type: application/json' --data '{"text":"Please see the follwing links for Handovers and Change Requests that may impact your shift."}' https://hooks.slack.com/services/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

# Messages for Handover:
curl -X POST -H 'Content-type: application/json' --data '{"text":"Handovers: https://mirantis.my.salesforce.com/00O2S000003g25h"}' https://hooks.slack.com/services/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

# Message for All Change Requests:
# https://mirantis.my.salesforce.com/00O2S000004INH1?cancelURL=%2F00O2S000004INH1
curl -X POST -H 'Content-type: application/json' --data '{"text":"All Change Requests: https://mirantis.my.salesforce.com/00O2S000004INH1?cancelURL=%2F00O2S000004INH1"}' https://hooks.slack.com/services/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

# Message for Change Requests in Ready to Execute
# https://mirantis.my.salesforce.com/00O2S000004ISIs
# curl -X POST -H 'Content-type: application/json' --data '{"text":"All CRs in Ready to Execute:
https://mirantis.my.salesforce.com/00O2S000004ISIs"}' https://hooks.slack.com/services/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

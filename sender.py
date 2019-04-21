from notion_client.collection import get_outdated_rows
from slack.format import SlackFormatter
import json
import requests

formatter = SlackFormatter()

def send_draft_message():
    rows = get_outdated_rows()
    sorted(rows, key=lambda x: x['days'], reverse=True)

    payload = formatter.notion_draft(rows)

    url = "https://hooks.slack.com/services/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"
    
    requests.post(url, json=payload)



send_draft_message()
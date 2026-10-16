"""Print (and optionally post to Slack) jobs that appeared since yesterday for a keyword.
Run it daily from cron or GitHub Actions (see .github/workflows/daily-alert.yml).
Env: APIFY_TOKEN, optional SLACK_WEBHOOK_URL, KEYWORDS="python,rust", COUNTRY=US"""
import os
import requests
from datetime import date, timedelta
from common import run_feed

keywords = [k.strip() for k in os.environ.get("KEYWORDS", "machine learning").split(",")]
since = (date.today() - timedelta(days=1)).isoformat()

new_jobs = [j for j in run_feed({
    "mode": "changes",
    "changeTypes": ["new"],
    "changesSince": since,
    "searchKeywords": keywords,
    "locations": [os.environ.get("COUNTRY", "US")],
    "descriptionMode": "none",
    "maxItems": 100,
})]
lines = [f"• {j['company']}: <{j['jobUrl']}|{j['title']}> ({j.get('location') or 'n/a'})" for j in new_jobs]
text = f"{len(new_jobs)} new jobs for {', '.join(keywords)} since {since}\n" + "\n".join(lines[:30])
print(text)

hook = os.environ.get("SLACK_WEBHOOK_URL")
if hook and new_jobs:
    requests.post(hook, json={"text": text}, timeout=20).raise_for_status()

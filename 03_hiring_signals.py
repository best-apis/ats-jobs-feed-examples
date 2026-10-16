"""Rank companies by how many roles they posted in the last 7 days in a function, e.g. to find sales triggers.
Usage: APIFY_TOKEN=... python 03_hiring_signals.py data"""
import sys
from common import run_feed

function = sys.argv[1] if len(sys.argv) > 1 else "data"
rows = list(run_feed({"mode": "companies", "functions": [function], "minOpenJobs": 5, "maxItems": 500}))
rows.sort(key=lambda r: r.get("postedLast7d") or 0, reverse=True)
print(f"Top companies hiring for '{function}' (jobs posted in the last 7 days):")
for r in rows[:20]:
    print(f"{r['company']:<35} 7d: {r['postedLast7d']:>4}  open: {r['openJobs']:>5}  remote: {r['remoteShare']:.0%}  {r['careersUrl']}")

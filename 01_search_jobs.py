"""Search the index and save the result to CSV.  Usage: APIFY_TOKEN=... python 01_search_jobs.py "data engineer" DE"""
import sys
import pandas as pd
from common import run_feed

keywords = sys.argv[1] if len(sys.argv) > 1 else "data engineer"
country = sys.argv[2] if len(sys.argv) > 2 else "DE"

items = list(run_feed({
    "mode": "jobs",
    "searchKeywords": [keywords],
    "locations": [country],
    "postedWithinDays": 14,
    "descriptionMode": "none",
    "maxItems": 200,
}))
df = pd.DataFrame(items)[["company", "title", "location", "workplace", "seniority", "salaryUsdYearMin", "salaryUsdYearMax", "postedAt", "jobUrl"]]
df.to_csv("jobs.csv", index=False)
print(f"{len(df)} jobs saved to jobs.csv")
print(df.head(10).to_string(index=False))

# ATS Jobs Feed: Python examples

Working examples for the [**ATS Jobs Feed**](https://apify.com/best_apis/ats-jobs-feed) Apify Actor: a daily-refreshed index of **350k+ open jobs from 12,000+ company career sites** (Greenhouse, Lever, Ashby, SmartRecruiters, Recruitee, Personio).

[![ATS Jobs Feed on Apify](https://apify.com/actor-badge?actor=best_apis/ats-jobs-feed)](https://apify.com/best_apis/ats-jobs-feed)

| Script | What it does |
|---|---|
| `01_search_jobs.py` | Keyword + country search to CSV |
| `02_daily_new_jobs_alert.py` | "New since yesterday" alert to stdout or Slack, plus a ready GitHub Actions cron (`examples/daily-alert.yml`: copy it to `.github/workflows/` in your own repo) |
| `03_hiring_signals.py` | Rank companies by roles posted in the last 7 days (sales triggers) |
| `04_salary_by_function.py` | Median advertised salary by function with pandas |

## Quick start
```bash
pip install -r requirements.txt
export APIFY_TOKEN=...        # free account: https://console.apify.com/account/integrations
python 01_search_jobs.py "data engineer" DE
APIFY_MAX_ITEMS=5 python 03_hiring_signals.py data   # cap results while experimenting
```
Runs are pay-per-result ($6 per 1,000 jobs, $0.005 per run); every script passes a max cost cap.

## Try it without an account
A free sample (3,800+ jobs, titles/companies/links only) and a data report: **https://best-apis.pages.dev/sample/**.

## Notes
- Data refreshes nightly; each record has `dataAsOf` and `snapshotId`.
- Postings that opted out of AI use are excluded by default. Employers can request removal via the Actor's Issues tab.
- Examples are MIT licensed. The data is subject to the Actor's terms.

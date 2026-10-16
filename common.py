"""Tiny helper: run the ATS Jobs Feed Actor and yield its dataset items."""
import os
from apify_client import ApifyClient

ACTOR = "best_apis/ats-jobs-feed"


def run_feed(run_input: dict, max_cost_usd: float = 1.0):
    # Optional global cap while experimenting: APIFY_MAX_ITEMS=5
    if os.environ.get("APIFY_MAX_ITEMS"):
        run_input = {**run_input, "maxItems": int(os.environ["APIFY_MAX_ITEMS"])}
    token = os.environ["APIFY_TOKEN"]
    client = ApifyClient(token)
    run = client.actor(ACTOR).call(run_input=run_input, max_total_charge_usd=max_cost_usd)
    return client.dataset(run.default_dataset_id).iterate_items()

"""Median advertised salary per job function for one country (pandas)."""
import pandas as pd
from common import run_feed

df = pd.DataFrame(run_feed({"mode": "jobs", "locations": ["US"], "minSalaryUsd": 1, "postedWithinDays": 30,
                            "descriptionMode": "none", "maxItems": 5000}, max_cost_usd=40))
df["mid"] = (df.salaryUsdYearMin + df.salaryUsdYearMax) / 2
print(df.groupby("function").mid.agg(["count", "median"]).query("count >= 30").sort_values("median", ascending=False).round(0))

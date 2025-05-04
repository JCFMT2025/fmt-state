# START_LOADER

import json

with open("fmt-state.json", "r") as f:
    state = json.load(f)

print("Current version:", state["metadata"]["version"])
print("Full market scan enabled:", state.get("full_market_scan_enabled"))

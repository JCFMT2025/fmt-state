# START_LOADER

import json
import urllib.request

with open("fmt-state.json", "r") as f:
    state = json.load(f)

# START_SPLIT_STATE_OVERRIDE
if state.get("metadata", {}).get("split_state_enabled"):
    core_path = state["metadata"]["core_state_path"]

    if core_path.startswith("http"):
        with urllib.request.urlopen(core_path) as response:
            state = json.load(response)
    else:
        with open(core_path, "r") as f:
            state = json.load(f)
# END_SPLIT_STATE_OVERRIDE

print("Current version:", state["metadata"]["version"])
print("Full market scan enabled:", state.get("full_market_scan_enabled"))

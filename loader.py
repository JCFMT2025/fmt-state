# START_LOADER

import json

with open("fmt-state.json", "r") as f:
    state = json.load(f)

# START_SPLIT_STATE_OVERRIDE
if state.get("metadata", {}).get("split_state_enabled"):
    with open(state["metadata"]["core_state_path"], "r") as f:
        state = json.load(f)
# END_SPLIT_STATE_OVERRIDE

print("Current version:", state["metadata"]["version"])
print("Full market scan enabled:", state.get("full_market_scan_enabled"))

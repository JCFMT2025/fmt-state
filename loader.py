# START_LOADER

import json
import requests

with open("fmt-state.json", "r") as f:
    state = json.load(f)

# START_SPLIT_STATE_OVERRIDE
if state.get("metadata", {}).get("split_state_enabled"):
    core_path = state["metadata"]["core_state_path"]

    if core_path.startswith("http"):
        print(f"🌐 Fetching from: {core_path}")
        response = requests.get(core_path)
        print("📦 Raw content returned:\n", response.text[:500])  # Show first 500 characters
        try:
            state = response.json()
        except Exception as e:
            print("❌ JSON decode error:", e)
            exit(1)
    else:
        with open(core_path, "r") as f:
            state = json.load(f)
# END_SPLIT_STATE_OVERRIDE

print("✅ Current version:", state["metadata"]["version"])
print("📊 Full market scan enabled:", state.get("full_market_scan_enabled"))

import json
import os
from datetime import datetime

# Load fixture filter input
with open("fixture-input.json", "r") as f:
    fixture_filter = json.load(f)["fixture_filter"]

# Fake FMS scan result (simulate the FMT engine logic)
scan_results = [
    {"market": "Match Winner", "selection": fixture_filter["teams"][0], "probability": 0.76},
    {"market": "Over 2.5 Goals", "selection": "Over", "probability": 0.65},
    {"market": "BTTS", "selection": "Yes", "probability": 0.61},
    {"market": "Correct Score", "selection": "2-1", "probability": 0.58},
    {"market": "First Goal", "selection": fixture_filter["teams"][0], "probability": 0.54}
]

# Sort predictions by probability
sorted_preds = sorted(scan_results, key=lambda x: x["probability"], reverse=True)

# Build full prediction result
output = {
    "predictions": {
        "top_5": sorted_preds[:5],
        "all": sorted_preds,
        "fixture_context": {
            "teams": fixture_filter["teams"],
            "competition": fixture_filter["competition"],
            "date_range": {
                "start": fixture_filter["date"],
                "end": fixture_filter["date_end"]
            }
        },
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
}

# Define paths (write to fmt-test-runner folder)
target_path = "../fmt-test-runner/fmt-history.json"
os.makedirs("../fmt-test-runner/predictions", exist_ok=True)

# Replace fmt-result-output.json
with open("../fmt-test-runner/predictions/fmt-result-output.json", "w") as f:
    json.dump(output["predictions"], f, indent=2)

# Update history log file
if os.path.exists(target_path):
    with open(target_path, "r") as f:
        history = json.load(f)
else:
    history = {
        "predictions": {},
        "prediction_log": []
    }

history["predictions"] = output["predictions"]
history["prediction_log"].append(output["predictions"])

with open(target_path, "w") as f:
    json.dump(history, f, indent=2)

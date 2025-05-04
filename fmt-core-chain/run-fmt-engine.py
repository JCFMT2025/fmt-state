import json
import os
from datetime import datetime

# Load fixture filter
with open("fixture-input.json", "r") as f:
    fixture_filter = json.load(f)["fixture_filter"]

# Simulate prediction results
scan_results = [
    {"market": "Match Winner", "selection": fixture_filter["teams"][0], "probability": 0.76},
    {"market": "Over 2.5 Goals", "selection": "Over", "probability": 0.65},
    {"market": "BTTS", "selection": "Yes", "probability": 0.61},
    {"market": "Correct Score", "selection": "2-1", "probability": 0.58},
    {"market": "First Goal", "selection": fixture_filter["teams"][0], "probability": 0.54}
]

sorted_preds = sorted(scan_results, key=lambda x: x["probability"], reverse=True)

# Create prediction result
result = {
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

# Define correct local output path for your app
local_path = "../fmt-test-runner/"
os.makedirs(local_path + "predictions", exist_ok=True)

# Save primary result
with open(local_path + "predictions/fmt-result-output.json", "w") as f:
    json.dump(result, f, indent=2)

# Update history file
history_file = local_path + "fmt-history.json"
if os.path.exists(history_file):
    with open(history_file, "r") as f:
        history = json.load(f)
else:
    history = {
        "predictions": {},
        "prediction_log": []
    }

history["predictions"] = result
history["prediction_log"].append(result)

with open(history_file, "w") as f:
    json.dump(history, f, indent=2)

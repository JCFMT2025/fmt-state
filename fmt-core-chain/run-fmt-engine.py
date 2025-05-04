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

# Prepare prediction payload
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

# Save the current prediction
os.makedirs("predictions", exist_ok=True)
with open("predictions/fmt-result-output.json", "w") as f:
    json.dump(output["predictions"], f, indent=2)

# Update fmt-history.json
history_path = "fmt-history.json"
if os.path.exists(history_path):
    with open(history_path, "r") as f:
        history = json.load(f)
else:
    history = {
        "predictions": {
            "top_5": [],
            "all": [],
            "fixture_context": {},
            "timestamp": ""
        },
        "prediction_log": []
    }

# Replace live view
history["predictions"] = output["predictions"]

# Append to log
history["prediction_log"].append(output["predictions"])

# Save updated history
with open(history_path, "w") as f:
    json.dump(history, f, indent=2)

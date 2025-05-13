import os
import json
import argparse
from datetime import datetime

# ──────────────────────────────────────────────
# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('--match', required=True, help='Match ID or slug')
parser.add_argument('--mode', default='standard', help='Run mode')
args = parser.parse_args()

match_id = args.match
mode = args.mode

print(f"🔧 Running FMT Engine for: {match_id} | Mode: {mode}")

# ──────────────────────────────────────────────
# Load core system state (new location)
with open('fmt-core-state.json', 'r') as f:
    fmt_state = json.load(f)

# ──────────────────────────────────────────────
# Dummy prediction output (simulate logic)
prediction = {
    "fixture": {
        "match_id": match_id,
        "date": datetime.utcnow().strftime('%Y-%m-%d'),
        "competition": "Sample League",
        "teams": ["Team A", "Team B"]
    },
    "predictions": [
        { "market": "Match Winner", "selection": "Team A", "probability": 0.72 },
        { "market": "Over 2.5 Goals", "selection": "Over", "probability": 0.66 },
        { "market": "Both Teams to Score", "selection": "Yes", "probability": 0.61 },
        { "market": "Correct Score", "selection": "2-1", "probability": 0.53 },
        { "market": "First Goal", "selection": "Team A", "probability": 0.57 }
    ]
}

# ──────────────────────────────────────────────
# Save to predictions/<match>.json
os.makedirs('predictions', exist_ok=True)
pred_path = f"predictions/{match_id}.json"
with open(pred_path, 'w') as f:
    json.dump(prediction, f, indent=2)
print(f"✅ Saved prediction: {pred_path}")

# ──────────────────────────────────────────────
# Save to fmt-history.json (Command Hub compatible structure)
history_file = 'fmt-history.json'
if os.path.exists(history_file):
    with open(history_file, 'r') as f:
        history = json.load(f)
else:
    history = { "predictions": {} }

history["predictions"][match_id] = {
    "timestamp": datetime.utcnow().isoformat(),
    "mode": mode,
    "file": pred_path
}

with open(history_file, 'w') as f:
    json.dump(history, f, indent=2)

print("📜 fmt-history.json updated with structured entry")

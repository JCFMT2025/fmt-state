import json
import sys
from datetime import datetime

def load_fixture_input(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data.get("fixture_filter", {})
    except Exception as e:
        print(f"❌ Failed to load fixture input: {e}")
        sys.exit(1)

def simulate_fmt_prediction(fixture):
    print("🔍 Running simulated FMT engine...")
    print(f"🏟️  Fixture: {fixture['teams'][0]} vs {fixture['teams'][1]}")
    print(f"📆 Date: {fixture['date']}")
    print(f"🏆 Competition: {fixture['competition']}")

    predictions = [
        {"market": "Match Winner", "selection": fixture["teams"][0], "probability": 0.76},
        {"market": "Over 2.5 Goals", "selection": "Over", "probability": 0.65},
        {"market": "BTTS", "selection": "Yes", "probability": 0.61},
        {"market": "Correct Score", "selection": "2-1", "probability": 0.58},
        {"market": "First Goal", "selection": fixture["teams"][0], "probability": 0.54}
    ]

    output = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "fixture": fixture,
        "predictions": predictions
    }

    with open("fmt-result-output.json", "w") as f:
        json.dump(output, f, indent=2)

    print("✅ Simulated FMT prediction written to fmt-result-output.json")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 run-fmt-engine.py fixture-input.json")
        sys.exit(1)

    fixture_data = load_fixture_input(sys.argv[1])
    simulate_fmt_prediction(fixture_data)

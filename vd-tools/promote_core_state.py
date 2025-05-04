import json
import os

LOADER_PATH = "loader.py"

# Logic to inject split-state override with URL support
SPLIT_PATCH = '''
# START_SPLIT_STATE_OVERRIDE
import urllib.request
core_path = state["metadata"]["core_state_path"]

if core_path.startswith("http"):
    with urllib.request.urlopen(core_path) as response:
        state = json.load(response)
else:
    with open(core_path, "r") as f:
        state = json.load(f)
# END_SPLIT_STATE_OVERRIDE
'''

def patch_loader():
    if not os.path.exists(LOADER_PATH):
        print(f"❌ {LOADER_PATH} not found.")
        return

    with open(LOADER_PATH, "r") as f:
        code = f.read()

    if "split_state_enabled" in code and "core_state_path" in code:
        print("✅ Loader already patched. No action taken.")
        return

    # Insert after loader start marker or default to top
    insert_point = code.find("# START_LOADER")
    if insert_point != -1:
        patched_code = code[:insert_point + len("# START_LOADER\n")] + SPLIT_PATCH + code[insert_point + len("# START_LOADER\n"):]
    else:
        patched_code = SPLIT_PATCH + code

    with open(LOADER_PATH, "w") as f:
        f.write(patched_code)

    print("✅ Patched loader.py with split-state override and URL support.")

if __name__ == "__main__":
    patch_loader()

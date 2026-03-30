import sys
import json
import os

def convert_windows_path(path, mappings):
    path = path.replace("\\", "/")
    drive = path[0]

    if drive in mappings:
        return mappings[drive] + path[2:]  # skip "Z:"
    return path

def convert_mac_path(path, mappings):
    path = path.rstrip("/")

    for local_root, linux_root in mappings.items():
        if path.startswith(local_root):
            relative = path[len(local_root):]
            return linux_root + relative

    return path

# Load mappings
with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "mappings.json")) as f:
    mappings = json.load(f)

input_path = sys.argv[1]

# Detect platform by path format
if ":" in input_path[:3]:  # Windows (e.g. Z:\)
    linux_path = convert_windows_path(input_path, mappings["windows"])
else:
    linux_path = convert_mac_path(input_path, mappings["mac"])

print(linux_path)
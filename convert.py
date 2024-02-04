import sys
import json
import os

def convert_windows_path_to_linux(windows_path):
    # Replace backslashes with forward slashes
    linux_path = windows_path.replace("\\", "/")
    
    # Remove Windows drive letter if present
    linux_path = linux_path.replace(":", "")

    return linux_path

def handle_drive_letter(path, mappings):
    drive = path[0]
    replacement = ""

    if (drive in mappings):
        return mappings[drive] + path[1:]
    else:
        return path[1:]
    match(drive):
        case "Y": 
            replacement = "/media/oldhdd"
        case "Z": 
            replacement = "/media/backupdrive"
        case "V": 
            replacement = "/media/oldbootdrive"
        case "X": 
            replacement = "/media/newerhdd"
        case "W": 
            replacement = "~"
    
    return replacement + path[1:]

mappings = {}
with open(os.path.dirname(os.path.realpath(__file__)) + "/mappings.json") as f:
    mappings = json.loads(f.read())

windows_path = sys.argv[1]
linux_path = handle_drive_letter(convert_windows_path_to_linux(windows_path), mappings)
print(linux_path)
#!/usr/bin/env python3

import os
import sys
from zipfile import ZipFile


if not os.path.exists("programming"):
    print("ERROR: programming folder not found; are you running this script from the folder containing the programming folder?")
    sys.exit(1)

corrected_tasks = []
for root, dirs, files in os.walk("programming"):
    for task in dirs:
        correction = os.path.join(root, task, "correction.py")
        if os.path.exists(correction):
            print(f"Found {task}/correction.py")
            corrected_tasks.append(correction)

if not corrected_tasks:
    print("no corrections found; did you create any correction.py files?")
    sys.exit(2)

with ZipFile('corrections.zip', 'w') as z:
    for correction in corrected_tasks:
        z.write(correction)
print("corrections.zip written successfully")


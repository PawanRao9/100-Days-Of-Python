import os
import re

# Get all files in the current directory
files = os.listdir()

# Regex to match files like day1.py to day99.py
pattern = re.compile(r'^day(\d+)\.py$', re.IGNORECASE)

for filename in files:
    match = pattern.match(filename)
    if match:
        day_num = int(match.group(1))
        new_name = f"day{day_num:02d}.py"
        if filename != new_name:
            os.rename(filename, new_name)
            print(f"Renamed {filename} → {new_name}")

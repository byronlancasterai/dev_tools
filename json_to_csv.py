#!/usr/bin/env python3
import json
import sys
import csv

# Read JSON from stdin
try:
    data = json.load(sys.stdin)
except json.JSONDecodeError:
    print("Error: Invalid JSON input", file=sys.stderr)
    sys.exit(1)

if not isinstance(data, list):
    print("Error: Input must be a list of objects", file=sys.stderr)
    sys.exit(1)

writer = csv.writer(sys.stdout)

if len(data) > 0:
    # Write header based on keys in first object
    headers = list(data[0].keys())
    writer.writerow(headers)
    
    for item in data:
        row = [item.get(key, '') for key in headers]
        writer.writerow(row)

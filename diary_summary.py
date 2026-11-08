#!/usr/bin/env python3
"""Read today's diary entries and print a one-line summary."""
import datetime
import os
import re

DIARY_PATH = os.path.expanduser("/config/byron/diary/2026-11-05.md")

def main():
    today = datetime.date.today().isoformat()
    entries = []
    with open(DIARY_PATH, "r") as f:
        for line in f:
            if line.startswith("## "):
                date_part = line[3:13]
                if date_part == today:
                    continue
                # skip non-today dates
                continue
            # simple approach: assume flat file with date headers
            # we'll just collect lines that start with a timestamp pattern
            pass

    # fallback: read whole file and filter by date string
    with open(DIARY_PATH, "r") as f:
        content = f.read()

    # diary entries look like: 17:07. Some text
    # we want entries from today
    lines = content.split("\n")
    todays = []
    for line in lines:
        m = re.match(r"^\d{2}:\d{2}\s+(.*)", line)
        if m:
            todays.append(m.group(1))

    if not todays:
        print("No diary entries found for today.")
        return

    print(f"{len(todays)} entries today:")
    for t in todays:
        print(f"  - {t}")

if __name__ == "__main__":
    main()

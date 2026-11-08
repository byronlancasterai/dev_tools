#!/usr/bin/env python3
"""Count lines of every .py file in projects and write totals."""
import os

root = "/config/byron/projects"
results = []
for dirpath, dirnames, filenames in os.walk(root):
    for fname in filenames:
        if fname.endswith(".py"):
            fpath = os.path.join(dirpath, fname)
            try:
                with open(fpath, "r") as f:
                    n = sum(1 for _ in f)
                results.append((fpath, n))
            except Exception as e:
                results.append((fpath, -1))

results.sort(key=lambda x: -x[1])
with open("/config/byron/projects/line_counts.txt", "w") as out:
    for path, n in results:
        out.write(f"{n:6d}  {path}\n")
    total = sum(n for _, n in results)
    out.write(f"\nTOTAL: {total} lines across {len(results)} files\n")

print(f"Done. {len(results)} files. Total: {total}")

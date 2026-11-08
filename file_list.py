#!/usr/bin/env python3
import json
from pathlib import Path

def list_files_json(path_str="."):
    path = Path(path_str)
    files = []
    try:
        for item in sorted(path.iterdir()):
            try:
                stat = item.stat()
                files.append({
                    "name": item.name,
                    "is_directory": item.is_dir(),
                    "is_file": item.is_file(),
                    "size": stat.st_size,
                    "modified": stat.st_mtime
                })
            except PermissionError:
                files.append({
                    "name": item.name,
                    "is_directory": item.is_dir(),
                    "is_file": item.is_file(),
                    "size": "permission denied",
                    "modified": None
                })
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        return
    print(json.dumps(files, indent=2))

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    list_files_json(target)

#!/usr/bin/env python3
"""Calculate total size of projects directory in MB."""
import os
import sys

def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)
    return total_size

path = '/config/byron/projects'
size_bytes = get_size(path)
size_mb = size_bytes / (1024 * 1024)

print(f"Total size: {size_mb:.2f} MB")

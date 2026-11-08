#!/usr/bin/env python3
"""List the most recently modified .py files in projects."""
import os
import datetime

PROJECTS_DIR = '/config/byron/projects'

def get_recent_files():
    files = []
    for root, dirs, filenames in os.walk(PROJECTS_DIR):
        # Skip venv and pycache directories to focus on my own work
        if 'venv' in root or '__pycache__' in root:
            continue
        for filename in filenames:
            if filename.endswith('.py'):
                filepath = os.path.join(root, filename)
                mtime = os.path.getmtime(filepath)
                files.append((mtime, filepath))
    
    # Sort by modification time descending
    files.sort(reverse=True)
    
    for mtime, filepath in files[:10]:
        dt = datetime.datetime.fromtimestamp(mtime)
        print(f"{dt.strftime('%Y-%m-%d %H:%M')}  {filepath}")

if __name__ == '__main__':
    get_recent_files()

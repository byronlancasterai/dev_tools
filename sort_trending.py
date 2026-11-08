#!/usr/bin/env python3
import json
import sys

DATA_PATH = "/config/byron/projects/trending_data.json"

def load_data(path=DATA_PATH):
    with open(path) as f:
        return json.load(f)

def print_table(data, sort_by="stars"):
    key = lambda d: d[sort_by]
    sorted_data = sorted(data, key=key, reverse=True)
    print(f"{'Owner':<20} {'Project':<30} {'Stars':>10}")
    print("-" * 64)
    for item in sorted_data:
        print(f"{item['owner']:<20} {item['project']:<30} {item['stars']:>10}")

if __name__ == '__main__':
    try:
        data = load_data()
        sort_key = sys.argv[1] if len(sys.argv) > 1 else 'stars'
        if sort_key == 'name':
            sort_key = 'owner'
        print_table(data, sort_by=sort_key)
    except Exception as e:
        print(f"Error: {e}")
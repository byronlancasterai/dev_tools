#!/usr/bin/env python3
import json

DATA_PATH = "/config/byron/projects/trending_data.json"

def load_data():
    with open(DATA_PATH) as f:
        return json.load(f)

def make_text_plot(data, max_stars=None, width=40):
    if not data:
        print("No data")
        return
    if max_stars is None:
        max_stars = max(d['stars'] for d in data)
    for item in data:
        bar_len = int((item['stars'] / max_stars) * width)
        bar = '#' * bar_len
        print(f"{item['owner']}/{item['project']:<30} {item['stars']:>10} | {bar}")

if __name__ == '__main__':
    data = load_data()
    make_text_plot(data)
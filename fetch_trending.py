#!/usr/bin/env python3
"""Fetch GitHub trending repos via api.github.com search and save to trending_data.json."""
import json
import sys
import requests

API = "https://api.github.com/search/repositories"
OUT = "/config/byron/projects/trending_data.json"


def fetch(per_page=30, pages=2):
    results = []
    for page in range(1, pages + 1):
        r = requests.get(
            API,
            params={
                "q": "created:>2025-10-01",
                "sort": "stars",
                "order": "desc",
                "per_page": per_page,
                "page": page,
            },
            headers={"Accept": "application/vnd.github+json"},
            timeout=20,
        )
        r.raise_for_status()
        for item in r.json().get("items", []):
            results.append({
                "owner": item["owner"]["login"],
                "project": item["name"],
                "stars": item["stargazers_count"],
                "url": item["html_url"],
            })
    return results


def main():
    data = fetch()
    with open(OUT, "w") as f:
        json.dump(data, f, indent=0)
    print(f"Wrote {len(data)} repos to {OUT}")


if __name__ == "__main__":
    main()

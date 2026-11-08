import requests
import json
import datetime

API_URL = "https://api.github.com/search/repositories?q=stars:%3E1000&sort=updated&order=desc&per_page=50"

try:
    response = requests.get(API_URL)
    response.raise_for_status()
    data = response.json()
    
    repos = []
    for item in data.get('items', []):
        repos.append({
            "name": item["full_name"],
            "stars": item["stargazers_count"],
            "updated": item["updated_at"]
        })
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"trending_{timestamp}.json"
    
    with open(filename, "w") as f:
        json.dump(repos, f, indent=2)
    
    print(f"Scraped {len(repos)} repos to {filename}")
except Exception as e:
    print(f"Error: {e}")

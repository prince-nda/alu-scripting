#!/usr/bin/python3
"""
Reddit API module
"""

import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "python:agent:v1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print("None")
        return
    
    try:
        data = response.json()
        posts = data["data"]["children"][:10]
        for post in posts:
            print(post["data"]["title"])
    except Exception:
        print("None")

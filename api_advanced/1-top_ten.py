#!/usr/bin/python3
"""Module to fetch top ten hot posts from a subreddit."""
import requests


def top_ten(subreddit):
    """Print titles of top 10 hot posts in subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyAPI/0.0.1"}
    params = {"limit": 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    
    if response.status_code == 200:
        data = response.json().get("data")
        children = data.get("children") if data else []
        if len(children) > 0:
            for child in children:
                print(child.get("data").get("title"))
        else:
            print("None")
    else:
        print("None")

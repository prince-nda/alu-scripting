#!/usr/bin/python3
"""Module that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a subreddit.

    Args:
        subreddit (str): the subreddit to query
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "MyRedditApp/0.1"}
    params = {"limit": 10}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get("data", {}).get("children", [])
        
        if posts:
            for i in range(min(10, len(posts))):
                print(posts[i]["data"]["title"])
        else:
            print("None")
    else:
        print("None")

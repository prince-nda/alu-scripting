#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    response = requests.get(url, headers=headers, timeout=5)
    
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            
            if posts:
                for post in posts:
                    title = post.get('data', {}).get('title')
                    if title:
                        print(title)
            else:
                print("None")
        except (ValueError, KeyError):
            print("None")
    else:
        print("None")

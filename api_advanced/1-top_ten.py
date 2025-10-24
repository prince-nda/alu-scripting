#!/usr/bin/python3
"""
Module to fetch top ten hot posts from a subreddit
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    
    Args:
        subreddit (str): The subreddit to query
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'python:subreddit.hot.posts:v1.0'}
    params = {'limit': 10}
    
    response = requests.get(url, headers=headers, params=params,
                          allow_redirects=False)
    
    if response.status_code == 200:
        try:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post['data']['title'])
            else:
                print("None")
        except (KeyError, ValueError):
            print("None")
    else:
        print("None")

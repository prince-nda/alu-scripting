#!/usr/bin/python3
"""
Reddit API Hot Posts Fetcher
"""

import requests


def top_ten(subreddit):
    """
    Prints titles of first 10 hot posts for given subreddit.
    
    Args:
        subreddit (str): Subreddit name to query
    """
    headers = {'User-Agent': 'python:reddit.hot.posts:v1.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}
    
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )
    
    if response.status_code != 200:
        print(None)
        return
    
    try:
        data = response.json()
        posts = data['data']['children']
        
        if len(posts) == 0:
            print(None)
            return
            
        for post in posts:
            print(post['data']['title'])
            
    except (KeyError, ValueError):
        print(None)

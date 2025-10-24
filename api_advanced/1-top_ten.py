#!/usr/bin/python3
import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit
    
    Returns:
        None: Prints titles or None if subreddit is invalid
    """
    # Set a custom User-Agent to avoid rate limiting
    headers = {
        'User-Agent': 'python:reddit.hot.posts.fetcher:v1.0 (by /u/your_username)'
    }
    
    # Reddit API URL for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    try:
        # Make GET request without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            
            # Extract posts from the response
            posts = data['data']['children']
            
            if not posts:
                print(None)
                return
            
            # Print titles of the first 10 hot posts
            for post in posts[:10]:
                title = post['data']['title']
                print(title)
                
        else:
            # If not 200 (could be 404, 302 redirect, etc.), print None
            print(None)
            
    except requests.exceptions.RequestException:
        print(None)
    except (KeyError, ValueError):
        # Handle JSON parsing errors or missing keys
        print(None)

# Example usage:
if __name__ == "__main__":
    # Test with valid subreddit
    top_ten("python")
    
    # Test with invalid subreddit
    top_ten("invalid_subreddit_that_does_not_exist")

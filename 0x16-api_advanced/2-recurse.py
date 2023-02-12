#!/usr/bin/python3
"""
Recursive function that queries the REDDIT API and returns a list containing
the titles of all hot articles for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[]):
    """ Returns a list containing the titles of all hot articles
        for a given subreddit, if no results are found for the
        given subreddit, the function returns None.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # User-Agent to avoid being blocked by the Reddit API
    headers = {"User-Agent": "RedditAPI Client"}

    # GET request to the REDDIT API to retrieve information about
    # hot articles in a given subreddit.
    response = requests.get(url, headers, allow_redirects=False)
    if response.status_code == 404:
        # if subreddit does not exist
        return None

    # parse the JSON data into a Python dictionary
    json_data = response.json()

    # Extract the list of hot articles from the JSON data returned
    hot_posts = json_data['data']['children']

    # Obtain title of every single hot article to the hot_list list.
    for post in hot_posts:
        host_list.append(post["data"]["title"])

    after = data["data"]["after"]

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list)

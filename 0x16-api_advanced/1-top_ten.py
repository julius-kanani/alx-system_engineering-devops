#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10
hot posts listed for a given subreddit.
"""


import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed for a given
        subreddit. If not a valid subreddit, prints None.
    """

    # set custom user-agent
    user_agent = "1011-BH"
    R_API = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    # custom user agent avoids request limit
    header = {"User-Agent": user_agent}

    req = requests.get(R_API, headers=header, allow_redirects=False)

    if req.status_code != 200:
        print('None')
    else:
        # load response unit from the request json
        data = req.json()['data']

        # extract list of pages
        posts = data['children']
        for post in posts:
            print(post['data']['title'])

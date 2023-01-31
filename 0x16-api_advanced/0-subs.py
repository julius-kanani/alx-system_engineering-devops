#!/usr/bin/python3
"""
How many subs?
Queries the Reddit API and returns the number of subscribers (not active
users, total subscribers) for a given subreddit.
Returns 0, If an invalid subreddit is given.
"""


import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers (not active users, total
        subscribers) for a given subreddit. If an invalid subreddit is
        given, the function returns 0.
    """

    REDDIT_API = "https://www.reddit.com/r/{}.json".format(subreddit)

    # set custom user-agent
    user_agent = "1011-BH"

    # custom user-agent avoids request limit
    header = {"User-Agent": user_agent}

    response = requests.get(REDDIT_API, headers=header, allow_redirects=False)

    if response.status_code != 200:
        return 0

    # load response from json
    data = response.json()['data']

    # extract list of pages
    pages = data['children']

    # extract data from first page
    page_data = pages[0]['data']

    # return number of subreddit subscribers
    return page_data['subreddit_subscribers']

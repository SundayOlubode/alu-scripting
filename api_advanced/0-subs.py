#!/usr/bin/python3
""" Reddit API """

import requests

def number_of_subscribers(subreddit):
    """ num of subscribers """
    url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)

    response = requests.get(url, \
    headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code != 200:
        return 0
    else:
        json_response = response.json()
        return json_response.get('data').get('subscribers')

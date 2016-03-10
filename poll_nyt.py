"""
poll_nyt.py

Basic strucutre adapted from https://github.com/mikedewar/RealTimeStorytelling/
"""

import json
import requests
from sys import stdout
from time import sleep
from config.secrets import NYT_NEWSWIRE_KEY

# Retrieves stories from the NY Times in all sections.
API_URL = 'http://api.nytimes.com/svc/news/v3/content/nyt/all'

seen_stories = set()

while True:

    response = requests.get(API_URL, params={
        'api-key': NYT_NEWSWIRE_KEY
    })

    data = response.json()
    for story in data.get('results'):
        item_type = story.get('item_type')
        updated_date = story.get('updated_date')
        url = story.get('url')

        # Ignore stories that we've seen before
        if (url, item_type, updated_date) in seen_stories:
            continue

        seen_stories.add((url, item_type, updated_date))

        print json.dumps({
            'item_type': item_type,
            'updated_date': updated_date,
            'url': url,
        })

    stdout.flush()

    # We are rate limited to 5000 requests a day to the newswire, so
    # 2 per minute * 60 min / hour * 24 hour / day = 2880 seems safe.
    sleep(30)

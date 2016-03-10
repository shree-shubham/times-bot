"""
poll_nyt.py

TODO

Basic strucutre adapted from https://github.com/mikedewar/RealTimeStorytelling/
"""

import json
import requests
from sys import stdout, stderr
from time import sleep
from config.secrets import NYT_COMMUNITY_KEY

# Retrieves stories from the NY Times in all sections.
API_URL = 'http://api.nytimes.com/svc/community/v3/user-content/recent.json'

seen_stories = set()
story_keys = ['commentID', 'commentTitle', 'createDate', 'commentBody',
              'userDisplayName']

while True:

    response = requests.get(API_URL, params={
        'api-key': NYT_COMMUNITY_KEY,
        'force-replies': 0
    })

    data = response.json()
    for story in data.get('results', {}).get('comments', [])[::-1]:
        filtered_story = {k:v for k,v in story.iteritems() if k in story_keys}

        # Ignore stories that we've seen before
        if filtered_story['commentID'] in seen_stories:
            continue

        seen_stories.add(filtered_story['commentID'])

        filtered_story['createDate'] = int(filtered_story['createDate'])

        stdout.write(json.dumps(filtered_story) + '\n')

    try:
        stdout.flush()
    except IOError as e:
        stderr.write(str(e) + '\n')

    # We are rate limited to 5000 requests a day to the community API, so
    # 2 per minute * 60 min / hour * 24 hour / day = 2880 req/day seems safe.
    sleep(2)

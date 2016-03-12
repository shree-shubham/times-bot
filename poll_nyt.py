"""
poll_nyt.py

Here, we poll for the latest comments from the NYT.

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
story_keys = ['commentID', 'commentTitle', 'updateDate', 'commentBody',
              'userDisplayName']

# poll forever.
while True:

    # Get the latest comments, and pull out the important info.
    response = requests.get(API_URL, params={
        'api-key': NYT_COMMUNITY_KEY,
        'force-replies': 0
    })

    data = response.json()
    stories = data.get('results', {}).get('comments', [])

    # Go in order of updateDate, so there won't be mitakes later.
    for story in sorted(stories, key=lambda x:x['updateDate']):
        # Filter for only the data we care about.
        filtered_story = {k:v for k,v in story.iteritems() if k in story_keys}

        # Ignore stories that we've seen before
        if filtered_story['commentID'] in seen_stories:
            continue
        seen_stories.add(filtered_story['commentID'])

        # Convert updateDate to an int.
        filtered_story['updateDate'] = int(filtered_story['updateDate'])

        # Write on to the next stage in the pipeline.
        stdout.write(json.dumps(filtered_story) + '\n')

    try:
        stdout.flush()
    except IOError as e:
        stderr.write(str(e) + '\n')

    # We are rate limited to 5000 requests a day to the community API, so
    # 3 per minute * 60 min / hour * 24 hour / day = 4320 req/day seems safe.
    sleep(20)

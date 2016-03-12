"""
insert.py

TODO

Basic strucutre adapted from https://github.com/mikedewar/RealTimeStorytelling/
"""

import json
import time
from sys import stdout, stdin
from redis import Redis

class ExpirationManager(object):
    # This is an approximation of the average time between comments in seconds. By
    # using this value, we attempt to remove entries from Redis at the same
    # frequently as we add them, keeping our database size relatively constant.
    AVG_TIME_BETWEEN_COMMENTS = 82

    def __init__(self):
        self.earliest_create_date = float('inf')
        self.start_time = time.time()

    def compute_expiration(self, story):
        """
        Computes an expiration intended to ensure that the redis database
        always has the same number of variables in it.  The first inserted will
        expire when the last one is inserted.

        ((startTime - earliestTime) + createTime + lifetime) - now
        """
        self.earliest_create_date = min(self.earliest_create_date,
                                        story['updateDate'])
        now = time.time()
        offset = self.start_time - self.earliest_create_date

        return int((story['updateDate'] +
                    offset +
                    self.AVG_TIME_BETWEEN_COMMENTS) - now)

conn = Redis()
conn.flushdb()
exp = ExpirationManager()

while True:
    # Read from line
    line = stdin.readline()
    story = json.loads(line)
    create_date = story['updateDate']
    # find the expiration we're going to be using.
    expiration = exp.compute_expiration(story)

    # Output to db.
    conn.hmset(create_date, story)
    conn.expire(create_date, expiration)

    # Print for records.
    print '[INSERT]', json.dumps({
        'create_date': create_date,
        'delta': story['delta'],
        'expiration': expiration,
        'body': story['commentBody']
    })

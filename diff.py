"""
diff.py

Computes the tie difference between this and the last update.

Basic strucutre adapted from https://github.com/mikedewar/RealTimeStorytelling/
"""

import json
from sys import stdout, stdin

last = None

while True:
    # Read from stdin
    line = stdin.readline()
    story = json.loads(line)

    # Handle edge case for the first data point.
    if last is None:
        last = story['updateDate']
        continue

    # Add 'delta' to the keys available on htheiiif
    story['delta'] = story['updateDate'] - last

    last = story['updateDate']

    # Print out into the pipeline
    stdout.write(json.dumps(story) + '\n')

    stdout.flush()

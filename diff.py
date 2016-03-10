"""
diff.py

DIFF

Basic strucutre adapted from https://github.com/mikedewar/RealTimeStorytelling/
"""

import json
from sys import stdout, stdin

last = None

while True:
    line = stdin.readline()
    story = json.loads(line)

    if last is None:
        last = story['createDate']
        continue

    story['delta'] = story['createDate'] - last

    last = story['createDate']

    stdout.write(json.dumps(story) + '\n')

    stdout.flush()

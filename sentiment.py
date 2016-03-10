"""

sentiment.py

Basic strucutre adapted from https://github.com/mikedewar/RealTimeStorytelling/

"""

import json
from sys import stdout, stdin

while 1:
    line = stdin.readline()
    story = json.loads(line)

    delta = d["t"] - last
    print json.dumps({"delta":delta, "t":d["t"]})
    stdout.flush()
    last = d["t"]

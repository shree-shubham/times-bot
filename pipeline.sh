#! /bin/bash

# Poll API -> Clean data -> Insert into Redis
python poll_nyt.py | python diff.py | python insert.py

"""
app.py

The main application logic.

Basic strucutre adapted from https://github.com/mikedewar/RealTimeStorytelling/
"""
from flask import Flask, render_template
from json_response import json_success
from stats import StatsManager
from collections import Counter
import math

# Holds database state
stats = StatsManager()

# Flask
app = Flask(__name__,
            static_folder='static/dist/',
            static_url_path='/static')
app.config.from_object('config.flask_config')

@app.route('/rate')
def rate():
    """Display the rate at which new comments are coming in."""
    return json_success({
        'rate': stats.get_rate()
    })

def buildHistogram():
    """Create a histogram of the data and display that."""
    values = stats.deltas
    c = Counter(values)
    z = sum(c.values())
    return {k:v/float(z) for k,v in c.items()}

@app.route('/')
def index():
    """Our sumamry / home page."""
    return render_template('index.html')

@app.route("/historgram")
def histogram():
    """A very small wrapper around the buildHistogram function, that allows the
    use of histograms in the API.
    """
    h = buildHistogram()
    return json_success(h)

@app.route("/entropy")
def entropy():
    """Display the entropy of our data set."""
    h = buildHistogram()
    return json_success({
        'entropy': -sum([p*math.log(p) for p in h.values()])
    })

@app.route('/probability/<n_seconds>')
def probabiltiy(n_seconds):
    """Display the probability that a comment occurs in the next 30 seconds."""
    h = buildHistogram()

    ## p = p_test / sum(p)
    total = sum(stats.deltas)
    z = float(n_seconds) / total
    return json_success({
        'probability': z
    })

@app.route('/data')
def data():
    """Simply print out all the data we have."""
    return json_success(stats.values)

if __name__ == '__main__':
    app.run()

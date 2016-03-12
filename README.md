# Times Bot

How crazy in the NYTimes right now?

Times Bot is built with [Flask][flask], [Gulp][gulp], and [SCSS][scss].

## Data

Example data:

```javascript
{
    "debug": {
        "version": 3.1
    },
    "status": "OK",
    "copyright": "Copyright (c) 2016 The New York Times Company.  All Rights Reserved.",
    "results": {
        "comments": [{
            "assetID": 3448909,
            "commentID": 17868516,
            "parentID": 17868183,
            "statusID": 2,
            "commentSequence": 17868516,
            "commentBody": "In addition, think about what it could do for the homelessness problem. Instead of someone being one rent payment away from becoming homeless, if they lost their job, another would be found instantly.  Landlords would know this and the whole landlord-tenant relationship would be transformed. Or, they could relocate with government assistance.",
            "commentTitle": "<br\/>",
            "createDate": "1457819086",
            "updateDate": "1457819108",
            "approveDate": "1457819108",
            "userID": 25036455,
            "userDisplayName": "jstevend",
            "userTitle": "NULL",
            "userURL": "NULL",
            "userLocation": "Mission Viejo, CA",
            "editorsSelection": 0,
            "recommendationCount": 0,
            "commentType": "userReply",
            "status": "approved",
            "asset": {
                "assetURL": "http:\/\/www.nytimes.com\/2016\/03\/13\/upshot\/the-geography-of-trumpism.html",
                "vendorID": "lK7pDDbSbDvIEb5jpy\/a1g==",
                "source": "url",
                "assetID": 3448909,
                "createDate": "1457788962",
                "updateDate": "1457819098",
                "taxonomies": [
                    [{
                        "taxonomyID": 316632,
                        "name": "upshot"
                    }, {
                        "taxonomyID": 363943,
                        "name": "The Geography of Trumpism (13up-trumpgeography)"
                    }]
                ],
                "taxonomy": "upshot\/The Geography of Trumpism (13up-trumpgeography)",
                "labels": [],
                "text": [],
                "properties": {
                    "comment-list-sort-approvedate-desc": {
                        "groupID": 1,
                        "taxonomyID": 1
                    },
                    "automoderation-on": {
                        "groupID": 2,
                        "taxonomyID": 316632
                    },
                    "reached-max-com-off": {
                        "groupID": 3,
                        "taxonomyID": 1
                    }
                },
                "all-properties": [{
                    "name": "no-group",
                    "description": "Not in a group",
                    "properties": []
                }, {
                    "name": "comment-list-sort",
                    "description": "Sort order to use when displaying comment listings",
                    "properties": {
                        "comment-list-sort-approvedate": {
                            "id": 2,
                            "description": "sort by approve date, oldest first"
                        },
                        "comment-list-sort-approvedate-desc": {
                            "id": 3,
                            "description": "sort by approve date, newest first"
                        },
                        "comment-list-sort-recommended": {
                            "id": 4,
                            "description": "sort by number of recommendations"
                        },
                        "comment-list-sort-editors": {
                            "id": 5,
                            "description": "sort by editors' selections"
                        },
                        "comment-list-sort-replies": {
                            "id": 6,
                            "description": "sort by replies"
                        }
                    }
                }, {
                    "name": "auto-moderation",
                    "description": "auto-moderation on or off",
                    "properties": {
                        "automoderation-on": {
                            "id": 7,
                            "description": "auto-moderation on"
                        },
                        "automoderation-off": {
                            "id": 8,
                            "description": "auto-moderation off"
                        }
                    }
                }, {
                    "name": "reached-max-com",
                    "description": "If we reached the max number of COMS per parent taxonomy",
                    "properties": {
                        "reached-max-com-on": {
                            "id": 9,
                            "description": "reached the max number of COMS"
                        },
                        "reached-max-com-off": {
                            "id": 10,
                            "description": "did not reach the max number of COMS"
                        }
                    }
                }, {
                    "name": "comment-style",
                    "description": "To use inline comments or overflow page",
                    "properties": {
                        "inline-comments": {
                            "id": 11,
                            "description": "articles having inline comments or overflow page"
                        },
                        "overflow": {
                            "id": 12,
                            "description": "comments on overflow page"
                        }
                    }
                }],
                "assetTitle": "The Geography of Trumpism (13up-trumpgeography)"
            },
            "replies": [],
            "display_name": "jstevend",
            "location": "Mission Viejo, CA"
        }, 

        ...
        
        ],
        "totalCommentsReturned": 25,
        "api_timestamp": "1457819125"
    }
}
```

Each of the elements in the `comments` array are comments recently created, updated, or approved on the New York Times websites.  I use this data to predict display how frequently comments are being posted on the new york times, and alert users when comment activity is especially high or low..  Data is used with permission from the [New York Times](http://developer.nytimes.com/).

## Routes of note:

- `/rate`: Display the rate at which new comments are coming in.

- `/`: Our sumamry / home page.

- `/historgram`: A very small wrapper around the buildHistogram function, that allows the use of histograms in the API

- `/entropy`: Display the entropy of our data set.

- `/probability/<n_seconds>`: Display the probability that a comment occurs in the next 30 seconds.

- `/data`: Simply print out all the data we have.

## Installation

1. Install node package manager (npm) by going to [nodejs.org][nodejs] and click INSTALL.
2. Install python package manager (pip) by going to [the pip install page](http://pip.readthedocs.org/en/stable/installing/#install-pip) and following the instructions there.

3. Check that `npm` is installed:

    ```bash
    npm -v
    ```

4. Check that `pip` is installed:

    ```bash
    pip -v
    ```

5. Install gulp globally

    ```bash
    npm install -g gulp
    ```

6. Install requirements

    ```bash
    cd when-will-the-1-come/
    npm install
    gem install sass scss_lint
    pip install virtualenv
    ```

7. Setup secrets file
    
**If you have a `secrets.py` file**: Simply place that file in the `config` folder. 

**Otherwise** run

```bash
cp config/example.secrets.py config/secrets.py
```

Then, edit `config/secrets.py` to contain the appropriate secret keys.

[nodejs]: https://nodejs.org/

## Running

### Printing to stdout

Type this command to print new data to the command line, without running the server.

```bash
./config/runserver.sh stdout
```

### Web Server

With one Gulp command, you can start the Flask server, and reload SCSS, JS, HTML, images, and fonts with Browserify:

```bash
gulp serve
```

## Gulp

An overview of Gulp commands available:

### `gulp build`

Builds the static parts of the site from the `app/static/src` into the `app/static/dist` directory.  This includes:

- SCSS w/ linting, sourcemaps and autoprefixing
- JS linting and uglification
- Image and font copying

### `gulp build:optimized`

This is used for distributing an optimized version of the site (for deployment).  It includes everything from `gulp build` as well as SCSS minification.

### `gulp watch`

Watchs for changes in local files and rebuilds parts of the site as necessary, into the `app/static/dist` directory.

### `gulp run`

Runs the Flask app in a virtual environment.

### `gulp serve`

Runs `gulp watch` in the background, and runs `gulp run`, proxying it to `localhost:3000` with automatic reloading using [Browsersync][browsersync].

## Structure

```
├── Gulpfile.js             # Controls Gulp, used for building the website
├── README.md               # This file
├── app                     # Root of the Flask application
│   ├── __init__.py         # Init the Flask app using the factory pattern
│   ├── forms.py            # Flask-WTForms forms and validators
│   ├── models.py           # Flask-SQLAlchemy models
│   ├── routes.py           # All URL routes
│   ├── static              # Static files
│   │   ├── dist            # The live static folder
│   │   └── src             # Source static files, will be copied into dist/
│   │       ├── font        # Font files
│   │       ├── img         # Images and SVGs
│   │       ├── js          # JavaScript libraries and scripts
│   │       └── sass        # Stylesheets
│   └── templates           # All Jinja templates / html
├── config                  
│   ├── example.secrets.py  # Example secrets file
│   ├── flask_config.py     # Global Flask config variables
│   ├── requirements.txt    # Python dependencies
│   ├── runserver.sh        # A script used by `gulp run` to run Flask
│   └── secrets.py          # .gitignore'd, file containing your secrets
├── manage.py               # Run this file to recreate the database
├── package.json            # JavaScript dependencies
└── run.py                  # Runs the Flask app.
```

[browsersync]: http://www.browsersync.io/
[gulp]: http://gulpjs.com/
[flask]: http://flask.pocoo.org/
[flask-sqlalchemy]: http://flask-sqlalchemy.pocoo.org/2.0/
[npm-install]: https://nodejs.org/en/download/
[scss]: http://sass-lang.com/


"""Configurations for this app."""
from sys import exit, stderr, argv

try:
    import secrets
    SECRET_KEY = secrets.SECRET_KEY
    NYT_NEWSWIRE_KEY = secrets.NYT_NEWSWIRE_KEY
    DEBUG = (len(argv) == 2 and argv[1] == 'debug')
    STDOUT = (len(argv) == 2 and argv[1] == 'stdout')
    META_TITLE = 'Happy Times'
    META_DESCRIPTION = (
        'Sometimes the Times are happy, sometimes they are sad.  We\'ll keep '
        'you informed with a web application that\'s rad.'
    )
    META_NAME = 'Happy Times'
    META_TWITTER_HANDLE = '@danrschlosser'
    META_DOMAIN = 'happytimes.schlosser.io'
    META_URL = 'http://' + META_DOMAIN
    META_IMAGE = 'static/img/favicon/mstile-310x150.png'

except ImportError:
    print >> stderr, 'Could not find config/secrets.py.  Do you have one?'
    exit(1)

except AttributeError as e:
    attr = e.message.lstrip('\'module\' object has no attribute ').rstrip('\'')
    print >> stderr, 'config/secrets.py is missing the key "%s"' % attr
    exit(1)

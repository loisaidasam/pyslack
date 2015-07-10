pyslack
==========

A Python wrapper for Slack's API

https://api.slack.com

Listed as an official python client on Slack's [Community-built Integrations page](https://api.slack.com/community)

## Installation

    pip install pyslack-real

([some chump](https://pypi.python.org/pypi/pyslack/) stole the `pyslack` name right out from under me!)

## Usage

Post a message into your Slack integration's `#play` channel

    >>> from pyslack import SlackClient
    >>> client = SlackClient('YOUR-TOKEN-HERE')
    >>> client.chat_post_message('#play', "testing, testing...", username='slackbot')
    {u'ok': 1, u'timestamp': u'1392000237000006'}


Integrate a SlackHandler into your logging!

    >>> import logging
    >>> from pyslack import SlackHandler
    
    >>> logger = logging.getLogger('test')
    >>> logger.setLevel(logging.DEBUG)
    
    >>> handler = SlackHandler('YOUR-TOKEN-HERE', '#channel_name', username='botname')
    >>> handler.setLevel(logging.WARNING)
    >>> formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(name)s (%(process)d): %(message)s')
    >>> handler.setFormatter(formatter)
    >>> logger.addHandler(handler)
    
    >>> logger.error("Oh noh!") # Will post the formatted message to channel #channel_name from user botname

## Testing

Before running the test suite, you'll need to add the required libraries to your environment. These aren't included in the main requirements.txt because they are not needed for normal operation of pyslack.

    pip install -r tests/requirements.txt
    
The tests can be run as follows:

    $ python setup.py test

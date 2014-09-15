pyslack
==========

A Python wrapper for Slack's API

https://api.slack.com

## Installation

    pip install git+git://github.com/loisaidasam/pyslack.git

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

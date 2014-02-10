pyslack
==========

A Python wrapper for Slack's API

https://api.slack.com

Examples:

    >>> from pyslack import SlackClient
    >>> client = SlackClient('YOUR-TOKEN-HERE')
    >>> client.chat_post_message('#play', "testing, testing...", username='slackbot')
    {u'ok': 1, u'timestamp': u'1392000237000006'}

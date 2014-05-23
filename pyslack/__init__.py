import logging
import requests


class SlackError(Exception):
    pass


class SlackClient(object):

    BASE_URL = 'https://slack.com/api'

    def __init__(self, token):
        self.token = token

    def _make_request(self, method, params):
        """Make request to API endpoint

        Note: Ignoring SSL cert validation due to intermittent failures
        http://requests.readthedocs.org/en/latest/user/advanced/#ssl-cert-verification
        """
        url = "%s/%s" % (SlackClient.BASE_URL, method)
        params['token'] = self.token
        result = requests.post(url, data=params, verify=False).json()
        if not result['ok']:
            raise SlackError(result['error'])
        return result

    def chat_post_message(self, channel, text, username=None, parse=None, link_names=None):
        """chat.postMessage

        This method posts a message to a channel.

        https://api.slack.com/methods/chat.postMessage
        """
        method = 'chat.postMessage'
        params = {
            'channel': channel,
            'text': text,
        }
        if username is not None:
            params['username'] = username
        if parse is not None:
            params['parse'] = parse
        if link_names is not None:
            params['link_names'] = link_names
        return self._make_request(method, params)


class SlackHandler(logging.Handler):
    """A logging handler that posts messages to a Slack channel!

    References:
    http://docs.python.org/2/library/logging.html#handler-objects
    """
    def __init__(self, token, channel, username=None, parse=None, link_names=None):
        super(SlackHandler, self).__init__()
        self.client = SlackClient(token)
        self.channel = channel
        self.username = username
        self.parse = parse
        self.link_names = link_names

    def emit(self, record):
        message = self.format(record)
        self.client.chat_post_message(self.channel,
                                      message,
                                      self.username,
                                      self.parse,
                                      self.link_names)

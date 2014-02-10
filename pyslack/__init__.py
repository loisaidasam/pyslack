
import requests


class SlackError(Exception):
    pass


class SlackClient(object):

    BASE_URL = 'https://slack.com/api'

    def __init__(self, token):
        self.token = token

    def _make_request(self, method, params):
        url = "%s/%s" % (SlackClient.BASE_URL, method)
        params['token'] = self.token
        result = requests.post(url, data=params).json()
        if not result['ok']:
            raise SlackError(result['error'])
        return result

    def chat_post_message(self, channel, text, username=None, parse=None, link_names=None):
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

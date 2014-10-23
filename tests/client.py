# coding: utf-8

import datetime
import unittest

from mock import Mock, patch

import pyslack


class ClientTest(unittest.TestCase):
    token = "my token"

    @patch('requests.post')
    def test_post_message(self, r_post):
        """A message can be posted to a channel"""
        client = pyslack.SlackClient(self.token)

        reply = {"ok": True}
        r_post.return_value.json = Mock(return_value = reply)

        result = client.chat_post_message('#channel', 'message')
        self.assertEqual(reply, result)

    @patch('requests.post')
    def test_error_response(self, r_post):
        """Server error messages are handled gracefully"""
        client = pyslack.SlackClient(self.token)

        reply = {"ok": False, "error": "There was an error"}
        r_post.return_value.json.return_value = reply

        with self.assertRaises(pyslack.SlackError) as context:
            client.chat_post_message('#channel', 'message')

        self.assertEqual(context.exception.message, reply["error"])

    @patch('requests.post')
    def test_rate_limit(self, r_post):
        """HTTP 429 Too Many Requests response is handled gracefully"""
        client = pyslack.SlackClient(self.token)

        reply = {"ok": False, "error": "Too many requests"}
        r_post.return_value = Mock(status_code=429, headers={'retry-after': 10})
        r_post.return_value.json.return_value = reply

        with self.assertRaises(pyslack.SlackError) as context:
            client.chat_post_message('#channel', 'message')

        self.assertEqual(r_post.call_count, 1)
        self.assertGreater(client.blocked_until, 
                datetime.datetime.utcnow() + datetime.timedelta(seconds=8))

        # A second send attempt should also throw, but without creating a request
        with self.assertRaises(pyslack.SlackError) as context:
            client.chat_post_message('#channel', 'message')

        self.assertEqual(r_post.call_count, 1)

        # After the time has expired, it should be business as usual
        client.blocked_until = datetime.datetime.utcnow() - \
                datetime.timedelta(seconds=5)

        r_post.return_value = Mock(status_code=200)
        r_post.return_value.json.return_value = {"ok": True}

        client.chat_post_message('#channel', 'message')
        self.assertEqual(r_post.call_count, 2)


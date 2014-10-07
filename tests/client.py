# coding: utf-8

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


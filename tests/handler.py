# coding: utf-8

import unittest
import logging

from mock import Mock, patch, ANY

import pyslack


class ClientTest(unittest.TestCase):
    token = "my token"

    @patch('pyslack.SlackClient.chat_post_message')
    def test_post_message(self, client_chatpostmessage):
        """Python log messages can be posted to a channel"""
        logger = logging.getLogger('test')
        logger.setLevel(logging.DEBUG)

        handler = pyslack.SlackHandler('my token', '#channel', username='botname')
        handler.setLevel(logging.WARNING)
        formatter = logging.Formatter('[%(levelname)s] %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        logger.error("Oh noh!")

        client_chatpostmessage.assert_called_with(
                '#channel', 
                '[ERROR] Oh noh!',
                username='botname')


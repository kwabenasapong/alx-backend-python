#!/usr/bin/env python3
'''
tasks
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    '''
    TestAccessNestedMap class
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''
        test_access_nested_map method
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_dict, path):
        '''
        test_access_nested_map_exception method
        '''
        with self.assertRaises(KeyError):
            access_nested_map(nested_dict, path)


class TestGetJson(unittest.TestCase):
    '''TestGetJson class'''
    @patch('utils.requests.get')
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload, mock_get):
        '''test_get_json method'''
        mock_get.return_value = Mock(json=lambda: test_payload)
        response = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)

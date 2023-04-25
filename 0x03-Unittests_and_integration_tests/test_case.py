#!/usr/bin/env python3

'''testing the test_utils.py file'''

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    '''testing the access_nested_map function'''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''test_access_nested_map method'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_dict, path):
        '''test_access_nested_map_exception method'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_dict, path)


class TestGetJson(unittest.TestCase):
    '''testing the get_json function'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        '''test_get_json method'''
        with patch('requests.get') as mock_get:
            mock_get.return_value = Mock()
            mock_get.return_value.json.return_value = test_payload
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    '''testing the memoize function'''

    def test_memoize(self):
        '''test_memoize method'''
        class TestClass:
            '''TestClass class'''

            def a_method(self):
                '''a_method method'''
                return 42

            @memoize
            def a_property(self):
                '''a_property method'''
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            test = TestClass()
            test.a_property
            test.a_property
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()

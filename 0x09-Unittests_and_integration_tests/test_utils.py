#!/usr/bin/env python3
"""TestAccessNestedMap module"""
from parameterized import parameterized
from utils import access_nested_map
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map function
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """ Test access_nested_map function for KeyError
        """
        self.assertRaises(KeyError)

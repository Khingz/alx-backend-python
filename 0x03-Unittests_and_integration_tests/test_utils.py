#!/bin/usr/env python3
"""Test package for utils module
"""
from utils import access_nested_map
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """test class for utils, access_nested method
    """
    @parameterized.expand([
        ({"a": 1}, ("a"), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            in_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
            ) -> None:
        """Connemt"""
        self.assertEqual(access_nested_map(in_map, path), expected)

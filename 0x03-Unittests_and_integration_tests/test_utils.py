#!/usr/bin/env python3
"""Test package for utils module
"""
from utils import (access_nested_map, get_json, memoize)
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            in_map: Dict,
            path: Tuple[str],
            exception: Exception,
            ) -> None:
        """Asser error"""
        with self.assertRaises(KeyError):
            (access_nested_map(in_map, path), exception)


class TestGetJson(unittest.TestCase):
    """Test class for json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(
            self,
            url: str,
            expected: Dict,
            ) -> None:
        """Test case for get_json
        """
        res = Mock()
        res.json.return_value = expected
        with patch("requests.get", return_value=res) as get_url:
            self.assertEqual(get_json(url), expected)
            get_url.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """TEST CLASS FOR MMOIZE
    """
    def test_momoize(self):
        """Test class
        """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                TestClass,
                'a_method',
                return_value=lambda: 42
                ) as m:
            obj = TestClass()
            res1 = obj.a_property()
            res2 = obj.a_property()
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)
            m.assert_called_once()

#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({'a': 1}, ("a", ), 1),
        ({'a': {'b': 2}}, ("a", ), {"b": 2}),
        ({'a': {'b': 2}}, ("a", "b"), 2),

    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a", )),
        ({'a': 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    # Test the get_json function with mocked HTTP requests
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        # Mock the response object and its json method
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload

        # Call the get_json function
        result = get_json(test_url)

        # Ensure the get method was called once with the correct URL
        mock_get.assert_called_once_with(test_url)

        # Ensure the result is equal to the mocked payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    # Test the memoize decorator
    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        test_obj = TestClass()

        # Use patch to mock a_method
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            # Call the memoized property twice
            result_1 = test_obj.a_property
            result_2 = test_obj.a_property

            # Assert that a_method was called only once
            mock_method.assert_called_once()

            # Ensure the result is correct
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/env python3
"""summary_line

Keyword arguments:
argument -- description
Return: return_description
"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("utils.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""

        # Define the mock return value for get_json
        mock_payload = {
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos"}
        mock_get_json.return_value = mock_payload

        # Create a GithubOrgClient instance
        client = GithubOrgClient(org_name)

        # Call org method
        org_data = client.org()

        # Ensure get_json was called with the expected argument
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

        # Check that org_data is as expected
        self.assertEqual(org_data, mock_payload)

    @patch("client.GithubOrgClient.org")
    def test_public_repos_url(self, mock_org):
        """Test the _public_repos_url property"""
        # Define a mock payload to be returned by org
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/google/repos"}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Check that _public_repos_url returns the expected value
        self.assertEqual(client._public_repos_url,
                         "https://api.github.com/orgs/google/repos")

    @patch("utils.get_json")
    @patch("client.GithubOrgClient._public_repos_url")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test the public_repos method"""
        # Mock data for public repos
        mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "Apache-2.0"}},
            {"name": "repo3", "license": {"key": "MIT"}}
        ]

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the public_repos method with MIT license filter
        repos = client.public_repos(license="MIT")

        # Ensure the list of repos matches the expected output
        self.assertEqual(repos, ["repo1", "repo3"])

        # Ensure that _public_repos_url was called once
        mock_public_repos_url.assert_called_once()

        # Ensure that get_json was called once with the correct URL
        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()

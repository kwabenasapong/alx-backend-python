#!/usr/bin/env python3

'''
test_client module - contains tests for the client module
'''

import unittest
from unittest.mock import patch, PropertyMock, Mock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    '''
    TestGithubOrgClient class
    '''
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, test_org_name, mock_get_json):
        '''
        test_org method
        '''
        test_class = GithubOrgClient(test_org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{test_org_name}'
        )

    def test_public_repos_url(self):
        '''
        test_public_repos_url method
        '''
        with patch.object(
            GithubOrgClient,
            'org',
            new_callable=PropertyMock,
            return_value={'repos_url': True}
        ) as mock_org:
            test_class = GithubOrgClient('test')
            result = test_class._public_repos_url
            self.assertEqual(result, mock_org.return_value['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        '''
        test_public_repos method
        '''
        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock,
            return_value='http://testurl.com'
        ) as mock_public_repos_url:
            mock_get_json.return_value = [{'name': 'Test'}]
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()
            self.assertEqual(result, ['Test'])
            mock_get_json.assert_called_once_with('http://testurl.com')
            mock_public_repos_url.assert_called_once_with()

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, expected):
        '''
        test_has_license method
        '''
        test_class = GithubOrgClient('test')
        result = test_class.has_license(repo, license_key)
        self.assertEqual(result, expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''
    TestIntegrationGithubOrgClient class
    '''
    @classmethod
    def setUpClass(cls):
        '''
        setUpClass method
        '''
        cls.get_patcher = patch('requests.get', side_effect=TEST_PAYLOAD)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        '''
        tearDownClass method
        '''
        cls.get_patcher.stop()

    def test_public_repos(self):
        '''
        test_public_repos method
        '''
        test_class = GithubOrgClient('test')
        self.assertEqual(test_class.org, TEST_PAYLOAD)
        self.assertEqual(test_class.public_repos_url,
                         TEST_PAYLOAD['repos_url'])
        self.assertEqual(test_class.public_repos(), TEST_PAYLOAD['repos_url'])
        self.assertEqual(test_class.public_repos()[
                         0]['name'], TEST_PAYLOAD['name'])
        self.assertEqual(test_class.public_repos()[
                         0]['license'], TEST_PAYLOAD['license'])
        self.assertEqual(test_class.public_repos()[
                         0]['license']['key'], TEST_PAYLOAD['license']['key'])

    def test_public_repos_with_license(self):
        '''
        test_public_repos_with_license method
        '''
        test_class = GithubOrgClient('test')
        self.assertEqual(test_class.org, TEST_PAYLOAD)
        self.assertEqual(test_class.public_repos_url,
                         TEST_PAYLOAD['repos_url'])

        self.assertEqual(test_class.public_repos(
            'apache-2.0'), TEST_PAYLOAD['repos_url'])
        self.assertEqual(test_class.public_repos('apache-2.0')
                         [0]['name'], TEST_PAYLOAD['name'])
        self.assertEqual(test_class.public_repos('apache-2.0')
                         [0]['license'], TEST_PAYLOAD['license'])
        self.assertEqual(test_class.public_repos('apache-2.0')
                         [0]['license']['key'], TEST_PAYLOAD['license']['key'])

        self.assertEqual(test_class.public_repos(
            'bsd'), TEST_PAYLOAD['repos_url'])
        self.assertEqual(test_class.public_repos('bsd')[
                         0]['name'], TEST_PAYLOAD['name'])
        self.assertEqual(test_class.public_repos('bsd')[
                         0]['license'], TEST_PAYLOAD['license'])
        self.assertEqual(test_class.public_repos('bsd')[
                         0]['license']['key'], TEST_PAYLOAD['license']['key'])

        self.assertEqual(test_class.public_repos(
            'gnu'), TEST_PAYLOAD['repos_url'])
        self.assertEqual(test_class.public_repos('gnu')[
                         0]['name'], TEST_PAYLOAD['name'])
        self.assertEqual(test_class.public_repos('gnu')[
                         0]['license'], TEST_PAYLOAD['license'])
        self.assertEqual(test_class.public_repos('gnu')[
                         0]['license']['key'], TEST_PAYLOAD['license']['key'])

        self.assertEqual(test_class.public_repos(
            'mit'), TEST_PAYLOAD['repos_url'])
        self.assertEqual(test_class.public_repos('mit')[
                         0]['name'], TEST_PAYLOAD['name'])
        self.assertEqual(test_class.public_repos('mit')[
                         0]['license'], TEST_PAYLOAD['license'])

        self.assertEqual(test_class.public_repos(
            'my_license'), TEST_PAYLOAD['repos_url'])
        self.assertEqual(test_class.public_repos('my_license')
                         [0]['name'], TEST_PAYLOAD['name'])
        self.assertEqual(test_class.public_repos('my_license')[
                         0]['license'], TEST_PAYLOAD['license'])
        self.assertEqual(test_class.public_repos('my_license')[
                         0]['license']['key'], TEST_PAYLOAD['license']['key'])

        self.assertEqual(test_class.public_repos(
            'other_license'), TEST_PAYLOAD['repos_url'])
        self.assertEqual(test_class.public_repos('other_license')[
                         0]['name'], TEST_PAYLOAD['name'])
        self.assertEqual(test_class.public_repos('other_license')[
                         0]['license'], TEST_PAYLOAD['license'])
        self.assertEqual(test_class.public_repos('other_license')[
                         0]['license']['key'], TEST_PAYLOAD['license']['key'])

        self.assertEqual(test_class.public_repos(
            'proprietary'), TEST_PAYLOAD['repos_url'])
        self.assertEqual(test_class.public_repos('proprietary')[
                         0]['name'], TEST_PAYLOAD['name'])
        self.assertEqual(test_class.public_repos('proprietary')[
                         0]['license'], TEST_PAYLOAD['license'])
        self.assertEqual(test_class.public_repos('proprietary')[
                         0]['license']['key'], TEST_PAYLOAD['license']['key'])

        self.assertEqual(test_class.public_repos(
            'wtfpl'), TEST_PAYLOAD['repos_url'])
        self.assertEqual(test_class.public_repos('wtfpl')[
                         0]['name'], TEST_PAYLOAD['name'])
        self.assertEqual(test_class.public_repos('wtfpl')[
                         0]['license'], TEST_PAYLOAD['license'])
        self.assertEqual(test_class.public_repos('wtfpl')[
                         0]['license']['key'], TEST_PAYLOAD['license']['key'])


if __name__ == '__main__':
    unittest.main()

from yadisk import create_folder
from parameterized import parameterized
import unittest

FIXTURE = [
    ('path', 201),
    ('path', 409),
    ('test1', 201)
]


def setup():
    print('setup')


def teardown():
    print('teardown')


class TestFunctionPytest(unittest.TestCase):
    @parameterized.expand(FIXTURE)
    def test_create_folder(self, path, result):
        self.assertEqual(create_folder(path), result)

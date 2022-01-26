import unittest
from unittest import mock
from py_order_utils.utils.utils import normalize


class TestUtils(unittest.TestCase):

    def test_normalize(self):
        self.assertEqual(normalize("aBcD%$EF"), "abcdef")
        


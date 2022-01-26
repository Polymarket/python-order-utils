import unittest
from unittest import mock
from py_order_utils.limit_order_builder import LimitOrderBuilder


class TestLimitOrderBuilder(unittest.TestCase):

    def test_hello(self):
        builder = LimitOrderBuilder()
        self.assertEqual(builder.hello(), "hello")
        pass


    pass


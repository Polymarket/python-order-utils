from unittest import TestCase
from py_order_utils.utils import generate_seed, normalize_address


class TestUtils(TestCase):

    def test_normalize_address(self):
        self.assertEqual(
            normalize_address("0x8b4de256180cfec54c436a470af50f9ee2813dbb"), 
            "0x8B4de256180CFEC54c436A470AF50F9EE2813dbB"
        )
    
    def test_generate_seed(self):
        self.assertIsNotNone(generate_seed())


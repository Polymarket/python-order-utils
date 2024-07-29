from unittest import TestCase
from py_order_utils.utils import generate_seed, normalize_address, prepend_zx


class TestUtils(TestCase):
    def test_normalize_address(self):
        self.assertEqual(
            normalize_address("0x8b4de256180cfec54c436a470af50f9ee2813dbb"),
            "0x8B4de256180CFEC54c436A470AF50F9EE2813dbB",
        )

    def test_generate_seed(self):
        self.assertIsNotNone(generate_seed())

    def test_prepend_zx(self):
        s = "302cd9abd0b5fcaa202a344437ec0b6660da984e24ae9ad915a592a90facf5a51bb8a873cd8d270f070217fea1986531d5eec66f1162a81f66e026db653bf7ce1c"
        self.assertEqual("0x" + s, prepend_zx(s))

        s = "02ca1d1aa31103804173ad1acd70066cb6c1258a4be6dada055111f9a7ea4e55"
        self.assertEqual("0x" + s, prepend_zx(s))

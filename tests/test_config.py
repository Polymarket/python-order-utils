from unittest import TestCase
from py_order_utils.config import COLLATERAL, EXCHANGE, EXECUTOR, get_contract_config

class TestConfig(TestCase):

    def test_get_config(self):
        valid_config = get_contract_config(42)
        self.assertIsNotNone(valid_config)
        self.assertIsNotNone(valid_config.get(EXCHANGE))
        self.assertIsNotNone(valid_config.get(EXECUTOR))
        self.assertIsNotNone(valid_config.get(COLLATERAL))
        
        
        # invalid config
        with self.assertRaises(Exception):
            get_contract_config(2190239023902)


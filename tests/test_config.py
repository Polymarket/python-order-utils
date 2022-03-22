from unittest import TestCase
from py_order_utils.config import get_contract_config

class TestConfig(TestCase):

    def test_get_config(self):
        valid_config = get_contract_config(80001)
        self.assertIsNotNone(valid_config)
        self.assertIsNotNone(valid_config.get_exchange())
        self.assertIsNotNone(valid_config.get_executor())
        self.assertIsNotNone(valid_config.get_collateral())
        
        
        # invalid config
        with self.assertRaises(Exception):
            get_contract_config(2190239023902)


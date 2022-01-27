from unittest import TestCase

import web3
from py_order_utils.facades.erc20_facade import Erc20Facade


class TestErc20Facade(TestCase):
    
    def setUp(self):
        self.facade = Erc20Facade()

    def test_balance_of(self):
        address = "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"
        expected = "0x70a08231000000000000000000000000ab5801a7d398351b8be11c439e05c5b3259aec9b"
        
        self.assertEqual(expected, self.facade.balance_of(address))

    def test_transfer_from(self):
        from_address = "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"
        to_address = "0x1Db3439a222C519ab44bb1144fC28167b4Fa6EE6"
        value = web3.Web3.toWei(100, 'ether')
        expected = "0x23b872dd000000000000000000000000ab5801a7d398351b8be11c439e05c5b3259aec9b0000000000000000000000001db3439a222c519ab44bb1144fc28167b4fa6ee60000000000000000000000000000000000000000000000056bc75e2d63100000"
        
        self.assertEqual(expected, self.facade.transfer_from(from_address, to_address, value))
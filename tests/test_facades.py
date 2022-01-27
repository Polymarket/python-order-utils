from unittest import TestCase

import web3
from py_order_utils.facades import Erc20Facade, Erc1155Facade , LimitOrderProtocolFacade

class TestFacade(TestCase):

    def setUp(self) -> None:
        self.erc20_facade = Erc20Facade()
        self.erc1155_facade = Erc1155Facade()
    
    def test_erc20_balance_of(self):
        address = "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"
        # Expected input data generated using ethers
        expected = "0x70a08231000000000000000000000000ab5801a7d398351b8be11c439e05c5b3259aec9b"

        self.assertEqual(expected, self.erc20_facade.balance_of(address))

    def test_erc20_transfer_from(self):
        from_address = "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"
        to_address = "0x1Db3439a222C519ab44bb1144fC28167b4Fa6EE6"
        value = web3.Web3.toWei(100, 'ether')
        # Expected input data generated using ethers
        expected = "0x23b872dd000000000000000000000000ab5801a7d398351b8be11c439e05c5b3259aec9b0000000000000000000000001db3439a222c519ab44bb1144fc28167b4fa6ee60000000000000000000000000000000000000000000000056bc75e2d63100000"
        
        self.assertEqual(expected, self.erc20_facade.transfer_from(from_address, to_address, value))

    def test_erc1155_balance_of(self):
        address = "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"
        token_id = 0
        # Expected input data generated using ethers
        expected = "0x00fdd58e000000000000000000000000ab5801a7d398351b8be11c439e05c5b3259aec9b0000000000000000000000000000000000000000000000000000000000000000"

        self.assertEqual(expected, self.erc1155_facade.balance_of(address, token_id))

    def test_erc1155_transfer_from(self):
        from_address = "0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B"
        to_address = "0x1Db3439a222C519ab44bb1144fC28167b4Fa6EE6"
        value = web3.Web3.toWei(100, 'ether')
        token_address = "0xadbeD21409324e0fcB80AE8b5e662B0C857D85ed"
        token_id = 0
        
        # Expected input data generated using ethers
        expected = "0x23b872e1000000000000000000000000ab5801a7d398351b8be11c439e05c5b3259aec9b0000000000000000000000001db3439a222c519ab44bb1144fc28167b4fa6ee60000000000000000000000000000000000000000000000056bc75e2d63100000000000000000000000000000adbed21409324e0fcb80ae8b5e662b0c857d85ed000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000"
        self.assertEqual(expected, self.erc1155_facade.transfer_from(from_address, to_address, token_address, token_id, value))

from enum import Enum
import json
import os
from web3 import Web3

from py_order_utils.utils import normalize_address

transferFrom = 'transferFrom'
balanceOf = 'balanceOf'
erc20Abi = "abi/ERC20ABI.json"

class Erc20Facade:

    def __init__(self, abi_file_path=erc20Abi):
        self.abi_file_path = abi_file_path
        self.web3 = Web3()
        self.contract = None

    def transfer_from(self, from_address, to_address, value : str):
        """
        Creates transaction data for an ERC20 transferFrom
        """
        return self._get_contract().encodeABI(fn_name=transferFrom, 
        args=[
            normalize_address(from_address), 
            normalize_address(to_address), 
            value
            ]
        )

    def balance_of(self, address):
        """
        Creates transaction data for an ERC20 balanceOf
        """
        return self._get_contract().encodeABI(fn_name=balanceOf, args=[normalize_address(address)])

    def _get_contract(self):
        if not self.contract:
            self.contract = self.web3.eth.contract(None, abi=self._get_abi())
        return self.contract
    
    def _get_abi(self):
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '..',
            self.abi_file_path,
        )

        with open(file_path, "r") as fh:
            abi = json.load(fh)
        return abi
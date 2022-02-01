import json
import os
from web3 import Web3

class BaseFacade:

    def __init__(self, contract_to_abi):
        self.contract_to_abi = contract_to_abi if contract_to_abi else {}
        self.web3 = Web3()
        self.contract = None

    def _get_contract(self, contract_name):
        if not self.contract:
            self.contract = self.web3.eth.contract(None, abi=self._get_abi(contract_name))
        return self.contract
    
    def _get_abi(self, contract_name):
        abi_file_path = self.contract_to_abi.get(contract_name.lower())
        if not abi_file_path:
            raise Exception("Contract ABI for {} not found".format(contract_name))
        
        file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '..',
            abi_file_path,
        )

        with open(file_path, "r") as fh:
            abi = json.load(fh)
        return abi
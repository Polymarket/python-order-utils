from ..utils import normalize_address
from .base_facade import BaseFacade


class Erc20Facade(BaseFacade):
    """
    Facade for ERC20 transfers and balance
    """
    
    ABIS = {"erc20": "abi/ERC20ABI.json"}

    def __init__(self):
        super().__init__(self.ABIS)

    def transfer_from(self, from_address, to_address, value : str):
        """
        Creates transaction data for an ERC20 transferFrom
        """
        return self._get_contract("erc20").encodeABI(fn_name="transferFrom", 
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
        return self._get_contract("erc20").encodeABI(fn_name="balanceOf", args=[normalize_address(address)])
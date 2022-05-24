import web3
from .base_facade import BaseFacade
from ..utils import normalize_address

class Erc1155Facade(BaseFacade):
    """
    Facade for ERC1155 transfers and balance
    """
    ABIS = {"erc1155": "abi/ERC1155ABI.json", "lop": "abi/PolyLimitOrderProtocol.json"}
    transferFrom = "func_733NCGU"
    balanceOf = "balanceOf"

    def __init__(self):
        super().__init__(self.ABIS)

    def transfer_from(self, from_address, to_address, token_address: str, token_id: str, value : str):
        """
        Creates transaction data for an ERC1155 transferFrom
        """
        
        return self._get_contract("lop").encodeABI(
            fn_name=self.transferFrom, 
            args=[
                normalize_address(from_address),
                normalize_address(to_address),
                value,
                normalize_address(token_address),
                token_id,
                web3.Web3.toBytes(hexstr="0x0")
                ]
        )

    def balance_of(self, address: str, token_id: str):
        """
        Creates transaction data for an ERC1155 balanceOf
        """
        return self._get_contract("erc1155").encodeABI(fn_name=self.balanceOf, args=[normalize_address(address), token_id])

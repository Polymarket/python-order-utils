from typing import List
from ..utils import normalize_address
from .base_facade import BaseFacade


class LimitOrderProtocolFacade(BaseFacade):
    """
    Limit Order protocol facade
    """
    
    ABIS = {"lop": "abi/PolyLimitOrderProtocol.json"}

    def __init__(self):
        super().__init__(self.ABIS)

    def lop_and(self, contract_address: str, predicates: List[str]):
        """
        function and(address[] calldata targets, bytes[] calldata data)
        """
        return self._get_contract("lop").encodeABI(
            fn_name="and", 
            args=[
                [normalize_address(contract_address) for _ in predicates],
                predicates,
            ]
        )
    
    def nonce_equals(self, maker_address: str, maker_nonce: int):
        """
        function nonceEquals(address makerAddress, uint256 makerNonce) external view returns(bool)
        """

        return self._get_contract("lop").encodeABI(
            fn_name="nonceEquals", 
            args=[
                maker_address,
                maker_nonce,
            ]
        )

    def timestamp_below(self, timestamp: int):
        """
        function timestampBelow(uint256 time) external view returns(bool)
        """
        return self._get_contract("lop").encodeABI(
            fn_name="timestampBelow", 
            args=[
                timestamp,
            ]
        )

    def get_maker_amount_data(self, maker_amount, taker_amount:int):
        """
        function getMakerAmount(uint256 orderMakerAmount, uint256 orderTakerAmount, uint256 swapTakerAmount) external pure returns(uint256)
        """
        return self._get_amount_data("getMakerAmount", maker_amount, taker_amount)

    def get_taker_amount_data(self, maker_amount, taker_amount:int):
        """
        function getTakerAmount(uint256 orderMakerAmount, uint256 orderTakerAmount, uint256 swapMakerAmount) external pure returns(uint256)
        """
        return self._get_amount_data("getTakerAmount", maker_amount, taker_amount)

    def _get_amount_data(self, method, maker_amount, taker_amount: int, swap_taker_amount=0):
        raw_amount_data = self._get_contract("lop").encodeABI(
            fn_name=method, 
            args=[
                maker_amount,
                taker_amount,
                swap_taker_amount
            ]
        )
        return raw_amount_data[:138]

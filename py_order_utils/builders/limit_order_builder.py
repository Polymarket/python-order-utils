from ..signer import Signer
from .base_builder import BaseBuilder
from .exception import ValidationException
from ..utils import generate_seed, normalize_address
from ..facades import Erc20Facade, Erc1155Facade, LimitOrderProtocolFacade
from ..model.model import LimitOrder, LimitOrderAndSignature, LimitOrderData


class LimitOrderBuilder(BaseBuilder):
    """
    Limit order builder
    """
    
    def __init__(self, exchange_address: str, chain_id: int, signer: Signer):
        super().__init__(exchange_address, chain_id, signer)
        self.erc20_facade = Erc20Facade()
        self.erc1155_facade = Erc1155Facade()
        self.lop_facade = LimitOrderProtocolFacade()
        
    def build_limit_order(self, data: LimitOrderData)-> LimitOrder:
        """
        Builds a limit order
        """
        if not self._validate_inputs(data):
            raise ValidationException("Invalid limit order inputs")
        
        if data.maker_asset_id is not None:
            maker_asset = data.exchange_address
            maker_asset_data = self.erc1155_facade.transfer_from(
                data.maker_address,
                data.taker_address,
                data.maker_asset_address,
                data.maker_asset_id,
                data.maker_amount
            )
        else:
            maker_asset = data.maker_asset_address
            maker_asset_data = self.erc20_facade.transfer_from(
                data.maker_address,
                data.taker_address,
                data.maker_amount
            )
        
        if data.taker_asset_id is not None:
            taker_asset = data.exchange_address
            taker_asset_data = self.erc1155_facade.transfer_from(
                data.taker_address,
                data.maker_address,
                data.taker_asset_address,
                data.taker_asset_id,
                data.taker_amount
            )
        else:
            taker_asset = data.taker_asset_address
            taker_asset_data = self.erc20_facade.transfer_from(
                data.taker_address,
                data.maker_address,
                data.taker_amount
            )
        
        predicate = data.predicate if(data.expiry is None and data.nonce is None) else self.lop_facade.lop_and(
                self.contract_address,
                [
                    self.lop_facade.timestamp_below(data.expiry),
                    self.lop_facade.nonce_equals(data.maker_address, data.nonce)
                ]
            )
        signer = data.signer if data.signer is not None else data.maker_address

        get_maker_amount = self.lop_facade.get_maker_amount_data(data.maker_amount, data.taker_amount)
        get_taker_amount = self.lop_facade.get_taker_amount_data(data.maker_amount, data.taker_amount)

        return LimitOrder(
            salt=data.salt if data.salt else generate_seed(),
            makerAsset=maker_asset,
            takerAsset=taker_asset,
            makerAssetData=maker_asset_data,
            takerAssetData=taker_asset_data,
            getMakerAmount=get_maker_amount,
            getTakerAmount=get_taker_amount,
            predicate=predicate,
            signer=signer,
            sigType=data.sig_type
        )


    def build_limit_order_signature(self, limit_order: LimitOrder):
        """
        Signs the Limit order
        """
        return self.sign(self._create_struct_hash(limit_order))

    def build_limit_order_and_signature(self, limit_order: LimitOrder, signature: str):
        return LimitOrderAndSignature(order=limit_order, signature=signature, orderType="limit")

    def create_limit_order(self, data: LimitOrderData):
        """
        Helper function to build and sign a limit order
        """
        order = self.build_limit_order(data)
        sig = self.build_limit_order_signature(order)
        return LimitOrderAndSignature(order=order, signature=sig, orderType="limit")

    def _validate_inputs(self, data:LimitOrderData)-> bool:
        return not (
            # ensure required values exist
            data.exchange_address is None or 
            data.maker_asset_address is None or 
            data.taker_asset_address is None or
            data.maker_address is None or
            data.maker_amount is None or
            data.taker_amount is None or
            # both maker and taker asset ids cannot be None
            (data.maker_asset_id is None and data.taker_asset_id is None) or
            # ensure that the exchange address is the same as the provided contract address
            normalize_address(data.exchange_address) != self.contract_address
        )

    

    


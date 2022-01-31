from ..signer import Signer
from ..utils import generate_seed, normalize_address
from .base_builder import BaseBuilder
from .exception import ValidationException
from ..model.model import MarketOrder, MarketOrderData


class MarketOrderBuilder(BaseBuilder):

    def __init__(self, exchange_address: str, chain_id: int, signer: Signer):
        super().__init__(exchange_address, chain_id, signer)

    def build_market_order(self, data: MarketOrderData)-> MarketOrder:
        """
        Builds a market order
        """
        if not self._validate_inputs(data):
            raise ValidationException("Invalid market order inputs")

        maker_asset_id = data.maker_asset_id if data.maker_asset_id is not None else -1
        taker_asset_id = data.taker_asset_id if data.taker_asset_id is not None else -1

        signer = data.signer if data.signer is not None else data.maker_address

        return MarketOrder(
            salt=data.salt if data.salt else generate_seed(),
            maker = data.maker_address(),
            makerAsset = data.maker_asset_address,
            makerAmount = data.maker_amount,
            makerAssetID = maker_asset_id,
            takerAsset = data.taker_asset_address,
            takerAssetID = taker_asset_id,
            signer= signer,
            sigType = data.sig_type
        )
        

    def build_market_order_signature(self, mkt_order: MarketOrder):
        """
        """
        pass

    def _validate_inputs(self, data: MarketOrderData)->bool:
        return not (
            # ensure required values exist
            data.exchange_address is None or 
            data.maker_asset_address is None or 
            data.taker_asset_address is None or
            data.maker_address is None or
            data.maker_amount is None or
            (data.maker_asset_id is None and data.taker_asset_id is None) or
            normalize_address(data.exchange_address) != self.contract_address
        )
        
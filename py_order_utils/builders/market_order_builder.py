from ..signer import Signer
from ..utils import generate_seed, normalize_address
from .base_builder import BaseBuilder
from .exception import ValidationException
from ..model.model import MarketOrder, MarketOrderAndSignature, MarketOrderData


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
            maker = data.maker_address,
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
        Signs a market order
        """
        normalized_mkt_order = self._normalize(mkt_order)
        return self.sign(self._create_struct_hash(normalized_mkt_order))


    def build_market_order_and_signature(self, mkt_order: MarketOrder, signature: str):
        """
        Returns the canonical market order and signature object used across processes
        """
        return MarketOrderAndSignature(mkt_order, signature, "market")

    def create_market_order(self, data: MarketOrderData):
        """
        Helper function to build and sign a market order
        """
        order = self.build_market_order(data)
        sig = self.build_market_order_signature(order)
        return MarketOrderAndSignature(order=order, signature=sig, orderType="market", minAmountReceived=data.min_amount_received)

    def _normalize(self, mkt_order: MarketOrder):
        return MarketOrder(
            salt= mkt_order["salt"],
            maker = mkt_order["maker"],
            makerAsset = mkt_order["makerAsset"],
            makerAmount = mkt_order["makerAmount"],
            makerAssetID = mkt_order["makerAssetID"] if mkt_order["makerAssetID"] >= 0 else 0,
            takerAsset = mkt_order["takerAsset"],
            takerAssetID = mkt_order["takerAssetID"] if mkt_order["takerAssetID"] >= 0 else 0,
            signer= mkt_order["signer"],
            sigType = mkt_order["sigType"]
        )

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
        
from dataclasses import dataclass
import json

from ..constants import ZERO_ADDRESS, ZX
from .signatures import EOA
from eip712_structs import Address, Bytes, EIP712Struct, Uint

@dataclass
class LimitOrderData:
    """
    Inputs to generate Limit orders
    """
    salt: int = None
    exchange_address: str = None
    maker_asset_address: str = None
    maker_asset_id: str = None
    taker_asset_address: str = None
    taker_asset_id: str = None
    maker_address: str = None
    taker_address: str = ZERO_ADDRESS
    maker_amount: int = None
    taker_amount: int = None
    expiry: int = None
    nonce: int = None
    signer: str = None
    sig_type: int = EOA
    predicate: str = ZX


class LimitOrder(EIP712Struct):
    """
    Limit Order
    """
    salt = Uint(256)
    makerAsset = Address() 
    takerAsset = Address()
    makerAssetData = Bytes()
    takerAssetData = Bytes()
    getMakerAmount = Bytes()
    getTakerAmount = Bytes()
    predicate = Bytes()
    signer= Address()
    sigType = Uint(256)

    def dict(self):
        return {
                "salt": self["salt"],
                "makerAsset": self["makerAsset"],
                "takerAsset": self["takerAsset"],
                "makerAssetData": self["makerAssetData"],
                "takerAssetData": self["takerAssetData"],
                "getMakerAmount": self["getMakerAmount"],
                "getTakerAmount": self["getTakerAmount"],
                "predicate": self["predicate"],
                "signer": self["signer"],
                "sigType": self["sigType"],
        }


@dataclass
class MarketOrderData:
    """
    Inputs to generate Market orders
    """
    salt: int = None
    exchange_address: str = None
    maker_asset_address: str = None
    maker_asset_id: int = None
    taker_asset_address: str = None
    taker_asset_id: int = None
    maker_address: str = None
    maker_amount: int = None
    signer: str = None
    sig_type: int = EOA
    min_amount_received: int = "0"

class MarketOrder(EIP712Struct):
    """
    Market Order
    """
    # NOTE: Important to keep in mind, fields are ordered
    salt = Uint(256)
    signer = Address()
    maker = Address()
    makerAsset = Address()
    makerAmount = Uint(256)
    makerAssetID = Uint(256)
    takerAsset = Address()
    takerAssetID = Uint(256)
    sigType = Uint(256)

    def dict(self):
        return {
            "salt": self["salt"],
            "signer": self["signer"],
            "maker": self["maker"],
            "makerAsset": self["makerAsset"],
            "makerAmount": str(self["makerAmount"]),
            "makerAssetID": str(self["makerAssetID"]),
            "takerAsset": self["takerAsset"],
            "takerAssetID": str(self["takerAssetID"]),
            "sigType": self["sigType"],
        }
    

@dataclass
class LimitOrderAndSignature:
    """
    Canonical Limit order and signature
    """
    order: LimitOrder
    signature: str
    orderType: str

    def dict(self):
        return {
            "order": self.order.dict(),
            "signature": self.signature,
            "orderType": self.orderType,
        }


@dataclass
class MarketOrderAndSignature:
    """
    Canonical Market order and signature
    """
    order: MarketOrder
    signature: str
    orderType: str
    minAmountReceived: str = "0"; # Optional slippage protection field

    def dict(self):
        return {
            "order": self.order.dict(),
            "signature": self.signature,
            "orderType": self.orderType,
            "minAmountReceived": str(self.minAmountReceived),
        }

from dataclasses import dataclass

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
    maker_asset_id: int = None
    taker_asset_address: str = None
    taker_asset_id: int = None
    maker_address: str = None
    taker_address: str = ZERO_ADDRESS
    maker_amount: int = None
    taker_amount: int = None
    expiry: int = None
    nonce: int = None
    signer: str = None
    sig_type: int = EOA
    predicate: str = ZX
    permit: str = ZX
    interaction: str = ZX


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
    permit = Bytes()
    interaction = Bytes()
    signer= Address()
    sigType = Uint(256)


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
    

@dataclass
class LimitOrderAndSignature:
    """
    Canonical Limit order and signature
    """
    order: LimitOrder
    signature: str
    orderType: str


@dataclass
class MarketOrderAndSignature:
    """
    Canonical Market order and signature
    """
    order: MarketOrder
    signature: str
    orderType: str
from dataclasses import dataclass

from py_order_utils.constants import ZERO_ADDRESS, ZX
from py_order_utils.model.signatures import SignatureType

@dataclass
class LimitOrderData:
    """
    Inputs to generate Limit orders
    """
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
    sig_type: SignatureType = SignatureType.EOA # Default to EOA sig type
    predicate: str = ZX
    permit: str = ZX
    interaction: str = ZX


@dataclass
class LimitOrder:
    """
    Limit Order
    """
    salt: int
    makerAsset: str 
    takerAsset: str
    makerAssetData: str
    takerAssetData: str 
    getMakerAmount: str
    getTakerAmount: str
    predicate: str
    permit: str
    interaction: str
    signer: str
    sigType: int
    
@dataclass
class MarketOrder:
    """
    Market Order object
    """
    salt: str
    maker: str
    makerAsset: str
    makerAmount: str
    makerAssetID: int
    takerAsset: str
    takerAssetID: int
    signer: str
    sigType: int
    

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
from dataclasses import dataclass

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
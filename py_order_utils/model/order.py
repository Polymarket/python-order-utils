from dataclasses import dataclass

from ..constants import ZERO_ADDRESS
from .signatures import EOA
from eip712_structs import Address, EIP712Struct, Uint


@dataclass
class OrderData:
    """
    Inputs to generate orders
    """

    maker: str = None
    """
    Maker of the order, i.e the source of funds for the order
    """

    taker: str = ZERO_ADDRESS
    """
    Address of the order taker. The zero address is used to indicate a public order
    """

    tokenId: str = None
    """
    Token Id of the CTF ERC1155 asset to be bought or sold.
    If BUY, this is the tokenId of the asset to be bought, i.e the makerAssetId
    If SELL, this is the tokenId of the asset to be sold, i.e the  takerAssetId
    """

    makerAmount: str = None
    """
    Maker amount, i.e the max amount of tokens to be sold
    """

    takerAmount: str = None
    """
    Taker amount, i.e the minimum amount of tokens to be received
    """

    side: int = None
    """
    The side of the order, BUY or SELL
    """

    feeRateBps: str = None
    """
    Fee rate, in basis points, charged to the order maker, charged on proceeds
    """

    nonce: str = "0"
    """
    Nonce used for onchain cancellations
    """

    signer: str = None
    """
    Signer of the order. Optional, if it is not present the signer is the maker of the order.
    """

    expiration: str = "0"
    """
    Timestamp after which the order is expired.
    Optional, if it is not present the value is '0' (no expiration)
    """

    signatureType: int = EOA
    """
    Signature type used by the Order. Default value 'EOA'
    """


class Order(EIP712Struct):
    """
    Order
    """

    # NOTE: Important to keep in mind, fields are ordered

    salt = Uint(256)
    """
    Unique salt to ensure entropy
    """

    maker = Address()
    """
    Maker of the order, i.e the source of funds for the order
    """

    signer = Address()
    """
    Signer of the order
    """

    taker = Address()
    """
    Address of the order taker. The zero address is used to indicate a public order
    """

    tokenId = Uint(256)
    """
    Token Id of the CTF ERC1155 asset to be bought or sold.
    If BUY, this is the tokenId of the asset to be bought, i.e the makerAssetId
    If SELL, this is the tokenId of the asset to be sold, i.e the  takerAssetId
    """

    makerAmount = Uint(256)
    """
    Maker amount, i.e the max amount of tokens to be sold
    """

    takerAmount = Uint(256)
    """
    Taker amount, i.e the minimum amount of tokens to be received
    """

    expiration = Uint(256)
    """
    Timestamp after which the order is expired
    """

    nonce = Uint(256)
    """
    Nonce used for onchain cancellations
    """

    feeRateBps = Uint(256)
    """
    Fee rate, in basis points, charged to the order maker, charged on proceeds
    """

    side = Uint(8)
    """
    The side of the order, BUY or SELL
    """

    signatureType = Uint(8)
    """
    Signature type used by the Order
    """

    def dict(self):
        return {
            "salt": self["salt"],
            "maker": self["maker"],
            "signer": self["signer"],
            "taker": self["taker"],
            "tokenId": self["tokenId"],
            "makerAmount": self["makerAmount"],
            "takerAmount": self["takerAmount"],
            "expiration": self["expiration"],
            "nonce": self["nonce"],
            "feeRateBps": self["feeRateBps"],
            "side": self["side"],
            "signatureType": self["signatureType"],
        }


@dataclass
class SignedOrder:
    """
    Order + Signature
    """

    order: Order
    signature: str

    def dict(self):
        d = self.order.dict()
        d["signature"] = self.signature
        if d["side"] == 0:
            d["side"] = "BUY"
        else: 
            d["side"] = "SELL"
        d["expiration"] = str(d["expiration"])
        d["nonce"] = str(d["nonce"])
        d["feeRateBps"] = str(d["feeRateBps"])
        d["makerAmount"] = str(d["makerAmount"])
        d["takerAmount"] = str(d["takerAmount"])
        d["tokenId"] = str(d["tokenId"])
        return d

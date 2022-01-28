NAME = "1inch Limit Order Protocol"

VERSION = "1"

EIP_712_DOMAIN = [
    {"name": "name", "type": "string"},
    {"name": "version", "type": "string"},
    {"name": "chainId", "type": "uint256"},
    {"name": "verifyingContract", "type": "address"},
]

ORDER_STRUCTURE= [
    {"name": "salt", "type": "uint256"},
    {"name": "makerAsset", "type": "address"},
    {"name": "takerAsset", "type": "address"},
    {"name": "makerAssetData", "type": "bytes"},
    {"name": "takerAssetData", "type": "bytes"},
    {"name": "getMakerAmount", "type": "bytes"},
    {"name": "getTakerAmount", "type": "bytes"},
    {"name": "predicate", "type": "bytes"},
    {"name": "permit", "type": "bytes"},
    {"name": "interaction", "type": "bytes"},
    {"name": "signer", "type": "address"},
    {"name": "sigType", "type": "uint256"}
]
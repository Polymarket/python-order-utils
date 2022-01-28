from enum import Enum

PROTOCOL_NAME = '1inch Limit Order Protocol'
PROTOCOL_VERSION = '1'
ZX = '0x'
ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'


class SignatureType(Enum):
    EOA = 0
    CONTRACT = 1
    POLY_PROXY = 2

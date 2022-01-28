from enum import Enum

class SignatureType(Enum):
    EOA = 0
    CONTRACT = 1
    POLY_PROXY = 2
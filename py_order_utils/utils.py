import math
import web3
from secrets import randbelow
from string import punctuation

max_int = math.pow(2, 32)

def normalize(s: str)-> str:
    lowered = s.lower()
    for p in punctuation:
        lowered = lowered.replace(p, "")
    return lowered

def normalize_address(address: str) -> str:
    return web3.Web3.toChecksumAddress(address)

def rand_int()-> int:
    """
    Cryptographically secure randInt
    """
    return randbelow(max_int)
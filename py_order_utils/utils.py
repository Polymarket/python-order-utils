import math
from eth_utils import to_checksum_address
from string import punctuation
from random import random
from datetime import datetime, timezone

max_int = math.pow(2, 32)


def normalize(s: str) -> str:
    lowered = s.lower()
    for p in punctuation:
        lowered = lowered.replace(p, "")
    return lowered


def normalize_address(address: str) -> str:
    return to_checksum_address(address)


def generate_seed() -> int:
    """
    Pseudo random seed
    """
    now = datetime.now().replace(tzinfo=timezone.utc).timestamp()
    return round(now * random())


def prepend_zx(in_str: str) -> str:
    """
    Prepend 0x to the input string if it is missing
    """
    s = in_str
    if len(s) > 2 and s[:2] != "0x":
        s = f"0x{s}"
    return s

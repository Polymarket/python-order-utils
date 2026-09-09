import math
import secrets
from eth_utils import to_checksum_address
from string import punctuation

max_int = math.pow(2, 32)

# Number of random bits used for an order salt.
#
# Capped at 53 because the CLOB wire contract carries `salt` as a JSON number.
# JSON numbers are IEEE-754 doubles for many consumers and represent integers
# exactly only up to 2**53 - 1, so a wider salt could be rounded during transport
# while the EIP-712 signature was produced over the original value. The peer
# would then reconstruct a different digest and reject the order as having an
# invalid signature. 53 bits still gives roughly 9.0e15 of collision space.
SALT_BITS = 53


def normalize(s: str) -> str:
    lowered = s.lower()
    for p in punctuation:
        lowered = lowered.replace(p, "")
    return lowered


def normalize_address(address: str) -> str:
    return to_checksum_address(address)


def generate_seed() -> int:
    """
    Generate a cryptographically random order salt.

    The salt is the only entropy that distinguishes two otherwise identical
    orders in the EIP-712 digest, so it is a security-relevant value: a
    predictable salt lets a third party precompute an order hash before it is
    broadcast, and a colliding salt produces a duplicate order hash.

    This previously returned ``round(timestamp * random())``. That had two
    defects. ``random.random()`` is the Mersenne Twister, which is not a
    cryptographically secure generator -- its entire 19937-bit state can be
    recovered from 624 consecutive outputs, after which every future salt is
    predictable. And the timestamp was computed as
    ``datetime.now().replace(tzinfo=timezone.utc)``, which relabels a naive
    local time as UTC instead of converting it, so the value was skewed by the
    local UTC offset. ``secrets`` draws from the operating system CSPRNG and
    needs no clock input at all.
    """
    return secrets.randbits(SALT_BITS)


def prepend_zx(in_str: str) -> str:
    """
    Prepend 0x to the input string if it is missing
    """
    s = in_str
    if len(s) > 2 and s[:2] != "0x":
        s = f"0x{s}"
    return s

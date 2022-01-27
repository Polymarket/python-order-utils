from string import punctuation
import web3

def normalize(s: str)-> str:
    lowered = s.lower()
    for p in punctuation:
        lowered = lowered.replace(p, "")
    return lowered

def normalize_address(address: str) -> str:
    return web3.Web3.toChecksumAddress(address)
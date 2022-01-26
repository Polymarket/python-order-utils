from string import punctuation

def normalize(s: str)-> str:
    lowered = s.lower()
    for p in punctuation:
        lowered = lowered.replace(p, "")
    return lowered

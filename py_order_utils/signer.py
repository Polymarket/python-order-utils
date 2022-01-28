import eth_account

class Signer:
    """
    Signs orders using a private key 
    """

    def __init__(self, key: str):
        self._key = key
        self.address = eth_account.Account.from_key(key).address
    
    def sign(self, struct_hash):
        """
        Signs an EIP712 struct hash
        """

        raise NotImplementedError()
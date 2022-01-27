import eth_account

class Signer:
    """
    Signs orders using a private key 
    """

    def __init__(self, key: str):
        self.key = key
        self.address = eth_account.Account.from_key(key).address
    
    def sign(self, message_hash):
        """
        TODO: signs an EIP712 message
        """

        raise NotImplementedError()
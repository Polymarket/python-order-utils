class ContractConfig:
    def __init__(self, exchange, executor, collateral, conditional):
        self.exchange = exchange
        self.executor = executor
        self.collateral = collateral
        self.conditional = conditional

    def get_exchange(self):
        return self.exchange
    
    def get_executor(self):
        return self.executor
    
    def get_collateral(self):
        return self.collateral

    def get_conditional(self):
        return self.conditional
    

CONFIG = {
    137: ContractConfig(
        exchange="", 
        executor="",  #TODO: update these
        collateral="0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
        conditional = "0x4d97dcd97ec945f40cf65f87097ace5ea0476045"
    ),

    80001: ContractConfig(
        exchange="0xe8DaCEd3A06A59ADADF804771d10684A6E536ffd", 
        executor="0xA15b04F6eb916f2e368Aeb17740a52b0379B8B6D", 
        collateral="0x2E8DCfE708D44ae2e406a1c02DFE2Fa13012f961",
        conditional = "0x7D8610E9567d2a6C9FBf66a5A13E9Ba8bb120d43"
    )
}

def get_contract_config(chainID: int)->ContractConfig:
    """
    Get the contract configuration for the chain
    """
    config = CONFIG.get(chainID)
    if config is None:
        raise Exception("Invalid chainID: ${}".format(chainID))
    
    return config



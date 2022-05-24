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
        exchange="0x6D486b31b5c0f724828Aff07c88606b213B0D196", 
        executor="0x6b0ab7A1E65ea6AE9072f6c45B4261ACDfB30827", 
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



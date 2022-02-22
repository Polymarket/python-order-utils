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
    42: ContractConfig(
        exchange="0xE7819d9745e64c14541732ca07CC3898670b7650", 
        executor="0x382E8f6a8404eB11aaFd9A5a0B11aa5A24e0830B", 
        collateral="0xe22da380ee6B445bb8273C81944ADEB6E8450422",
        conditional = ""
    ),

    137: ContractConfig(
        exchange="", 
        executor="",  #TODO: update these
        collateral="0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
        conditional = "0x4d97dcd97ec945f40cf65f87097ace5ea0476045"
    ),

    80001: ContractConfig(
        exchange="0xA6227994182d87680a8d66F41ad7E3a56130858E", 
        executor="0x859876dD2683Df7AdBd8B8623Ce7F57Ea01f85Ad", 
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



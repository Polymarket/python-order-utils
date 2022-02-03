class ContractConfig:
    def __init__(self, exchange, executor, collateral):
        self.exchange = exchange
        self.executor = executor
        self.collateral = collateral

    def get_exchange(self):
        return self.exchange
    
    def get_executor(self):
        return self.executor
    
    def get_collateral(self):
        return self.collateral
    

CONFIG = {
    42: ContractConfig(
        exchange="0xE7819d9745e64c14541732ca07CC3898670b7650", 
        executor="0x382E8f6a8404eB11aaFd9A5a0B11aa5A24e0830B", 
        collateral="0xe22da380ee6B445bb8273C81944ADEB6E8450422"
    ),

    137: ContractConfig(
        exchange="0xE7819d9745e64c14541732ca07CC3898670b7650", 
        executor="0x382E8f6a8404eB11aaFd9A5a0B11aa5A24e0830B", 
        collateral="0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
    ),

    80001: ContractConfig(
        exchange="", 
        executor="", 
        collateral=""
    ),
}

def get_contract_config(chainID: int)->ContractConfig:
    """
    Get the contract configuration for the chain
    """
    config = CONFIG.get(chainID)
    if config is None:
        raise Exception("Invalid chainID: ${}".format(chainID))
    
    return config



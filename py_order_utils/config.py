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


def get_contract_config(chainID: int) -> ContractConfig:
    """
    Get the contract configuration for the chain
    """
    CONFIG = {
        137: ContractConfig(
            exchange="0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E",
            executor="0xb2a29463Df393a4CAef36541544715e6B48b80B7",
            collateral="0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174",
            conditional="0x4D97DCd97eC945f40cF65F87097ACe5EA0476045",
        ),
        80001: ContractConfig(
            exchange="0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E",
            executor="0xb2a29463Df393a4CAef36541544715e6B48b80B7",
            collateral="0x2E8DCfE708D44ae2e406a1c02DFE2Fa13012f961",
            conditional="0x7D8610E9567d2a6C9FBf66a5A13E9Ba8bb120d43",
        ),
    }

    config = CONFIG.get(chainID)
    if config is None:
        raise Exception("Invalid chainID: ${}".format(chainID))

    return config

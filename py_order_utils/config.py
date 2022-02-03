
EXCHANGE = "exchange"
EXECUTOR = "executor"
COLLATERAL = "collateral"

CONFIG = {
    42: { # KOVAN
        EXCHANGE: "0xE7819d9745e64c14541732ca07CC3898670b7650",
        EXECUTOR: "0x382E8f6a8404eB11aaFd9A5a0B11aa5A24e0830B",
        COLLATERAL: "0xe22da380ee6B445bb8273C81944ADEB6E8450422"
    },

    137: { # MATIC
        EXCHANGE: "",
        EXECUTOR: "",
        COLLATERAL: "0x2791Bca1f2de4661ED88A30C99A7a9449Aa84174"
    },

    80001: { # MUMBAI
    EXCHANGE: "",
    EXECUTOR: "",
    COLLATERAL: ""
    },
}

def get_contract_config(chainID: int):
    """
    Get the contract configuration for the chain
    """
    config = CONFIG.get(chainID)
    if config is None:
        raise Exception("Invalid chainID: ${}".format(chainID))
    
    return config



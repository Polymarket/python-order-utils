from dataclasses import dataclass

@dataclass
class ContractConfig:
    """
    Contract Configuration
    """

    exchange: str
    """
    The exchange contract responsible for matching orders
    """

    collateral: str
    """
    The ERC20 token used as collateral for the exchange's markets
    """

    conditional: str
    """
    The ERC1155 conditional tokens contract
    """

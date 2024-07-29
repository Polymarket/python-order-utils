from ..signer import Signer
from ..utils import normalize_address, prepend_zx
from poly_eip712_structs import make_domain, EIP712Struct
from eth_utils import keccak


class BaseBuilder:
    def __init__(
        self, exchange_address: str, chain_id: int, signer: Signer, salt_generator
    ):
        self.contract_address = normalize_address(exchange_address)
        self.signer = signer
        self.chain_id = chain_id
        self.domain_separator = self._get_domain_separator(
            self.chain_id, self.contract_address
        )
        self.salt_generator = salt_generator

    def _get_domain_separator(
        self, chain_id: int, verifying_contract: str
    ) -> EIP712Struct:
        return make_domain(
            name="Polymarket CTF Exchange",
            version="1",
            chainId=str(chain_id),
            verifyingContract=verifying_contract,
        )

    def _create_struct_hash(self, order: EIP712Struct):
        """
        Creates an EIP712 compliant struct hash for the Order
        """
        return prepend_zx(
            keccak(order.signable_bytes(domain=self.domain_separator)).hex()
        )

    def sign(self, struct_hash):
        """
        Signs the struct hash
        """
        return self.signer.sign(struct_hash)

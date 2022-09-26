from unittest import TestCase
from py_order_utils.builders.exception import ValidationException
from py_order_utils.model.order import OrderData
from py_order_utils.model.sides import BUY
from py_order_utils.builders import OrderBuilder
from py_order_utils.model.signatures import EOA
from py_order_utils.signer import Signer
from py_order_utils.config import get_contract_config
from py_order_utils.constants import ZERO_ADDRESS

# publicly known private key
private_key = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
signer = Signer(key=private_key)
maker_address = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
salt = 479249096354
chain_id = 80001
mumbai_contracts = get_contract_config(chain_id)


def mock_salt_generator():
    return salt


class TestOrderBuilder(TestCase):
    def test_validate_order(self):
        builder = OrderBuilder(mumbai_contracts.exchange, chain_id, signer)

        # Valid order
        data = self.generate_data()
        self.assertTrue(builder._validate_inputs(data))

        # Invalid if any of the required fields are missing
        data = self.generate_data()
        data.maker = None
        self.assertFalse(builder._validate_inputs(data))

        # Invalid if any of the required fields are invalid
        data = self.generate_data()
        data.nonce = "-1"
        self.assertFalse(builder._validate_inputs(data))

        data = self.generate_data()
        data.expiration = "not a number"
        self.assertFalse(builder._validate_inputs(data))

        # Invalid signature type
        data = self.generate_data()
        data.signatureType = 100
        self.assertFalse(builder._validate_inputs(data))

    def test_build_order(self):
        builder = OrderBuilder(mumbai_contracts.exchange, chain_id, signer)

        invalid_data_input = self.generate_data()
        invalid_data_input.tokenId = None

        # throw if invalid order input
        with self.assertRaises(ValidationException):
            builder.build_order(invalid_data_input)

        invalid_data_input = self.generate_data()
        invalid_data_input.signer = ZERO_ADDRESS

        # throw if invalid signer
        with self.assertRaises(ValidationException):
            builder.build_order(invalid_data_input)

        _order = builder.build_order(self.generate_data())

        # Ensure correct values on  order
        self.assertTrue(isinstance(_order["salt"], int))
        self.assertEqual(maker_address, _order["maker"])
        self.assertEqual(maker_address, _order["signer"])
        self.assertEqual(ZERO_ADDRESS, _order["taker"])
        self.assertEqual(1234, _order["tokenId"])
        self.assertEqual(100000000, _order["makerAmount"])
        self.assertEqual(50000000, _order["takerAmount"])
        self.assertEqual(0, _order["expiration"])
        self.assertEqual(0, _order["nonce"])
        self.assertEqual(100, _order["feeRateBps"])
        self.assertEqual(BUY, _order["side"])
        self.assertEqual(EOA, _order["signatureType"])

        # specific salt
        builder = OrderBuilder(
            mumbai_contracts.exchange, chain_id, signer, mock_salt_generator
        )

        _order = builder.build_order(self.generate_data())

        # Ensure correct values on order
        self.assertTrue(isinstance(_order["salt"], int))
        self.assertEqual(salt, _order["salt"])
        self.assertEqual(maker_address, _order["maker"])
        self.assertEqual(maker_address, _order["signer"])
        self.assertEqual(ZERO_ADDRESS, _order["taker"])
        self.assertEqual(1234, _order["tokenId"])
        self.assertEqual(100000000, _order["makerAmount"])
        self.assertEqual(50000000, _order["takerAmount"])
        self.assertEqual(0, _order["expiration"])
        self.assertEqual(0, _order["nonce"])
        self.assertEqual(100, _order["feeRateBps"])
        self.assertEqual(BUY, _order["side"])
        self.assertEqual(EOA, _order["signatureType"])

    def test_build_prder_signature(self):
        builder = OrderBuilder(
            mumbai_contracts.exchange, chain_id, signer, mock_salt_generator
        )

        _order = builder.build_order(self.generate_data())

        # Ensure struct hash is expected(generated via ethers)
        expected_struct_hash = (
            "0xbf58957703791db2ab057528d03d1cff5375d9a475b14a9073bb7d892398dc96"
        )
        struct_hash = builder._create_struct_hash(_order)
        self.assertEqual(expected_struct_hash, struct_hash.hex())

        expected_signature = "0x3874d2cfe79c0e82577f4f76ec58d950522ee5923a6f08441927d382c8178a5a2190fd4d5c49705e94d75999a58ec843f94a432e87ebc15cdb2186d315b3cc201b"
        sig = builder.build_order_signature(_order)
        self.assertEqual(expected_signature, sig)

    def test_build_signed_order(self):
        builder = OrderBuilder(
            mumbai_contracts.exchange, chain_id, signer, mock_salt_generator
        )

        signed_order = builder.build_signed_order(self.generate_data())

        expected_signature = "0x3874d2cfe79c0e82577f4f76ec58d950522ee5923a6f08441927d382c8178a5a2190fd4d5c49705e94d75999a58ec843f94a432e87ebc15cdb2186d315b3cc201b"
        self.assertEqual(expected_signature, signed_order.signature)
        self.assertTrue(isinstance(signed_order.order["salt"], int))
        self.assertEqual(salt, signed_order.order["salt"])
        self.assertEqual(maker_address, signed_order.order["maker"])
        self.assertEqual(maker_address, signed_order.order["signer"])
        self.assertEqual(ZERO_ADDRESS, signed_order.order["taker"])
        self.assertEqual(1234, signed_order.order["tokenId"])
        self.assertEqual(100000000, signed_order.order["makerAmount"])
        self.assertEqual(50000000, signed_order.order["takerAmount"])
        self.assertEqual(0, signed_order.order["expiration"])
        self.assertEqual(0, signed_order.order["nonce"])
        self.assertEqual(100, signed_order.order["feeRateBps"])
        self.assertEqual(BUY, signed_order.order["side"])
        self.assertEqual(EOA, signed_order.order["signatureType"])

    def generate_data(self) -> OrderData:
        return OrderData(
            maker=maker_address,
            taker=ZERO_ADDRESS,
            tokenId="1234",
            makerAmount="100000000",
            takerAmount="50000000",
            side=BUY,
            feeRateBps="100",
            nonce="0",
        )

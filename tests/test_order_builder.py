from unittest import TestCase
from py_order_utils.builders.exception import ValidationException
from py_order_utils.model.order import OrderData
from py_order_utils.model.sides import BUY
from py_order_utils.builders import OrderBuilder
from py_order_utils.model.signatures import EOA
from py_order_utils.signer import Signer
from py_order_utils.constants import ZERO_ADDRESS

# publicly known private key
private_key = "0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80"
signer = Signer(key=private_key)
maker_address = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"
salt = 479249096354
chain_id = 80002
amoy_contracts = {
    "exchange": "0xdFE02Eb6733538f8Ea35D585af8DE5958AD99E40",
    "negRiskExchange": "0xC5d563A36AE78145C45a50134d48A1215220f80a",
    "collateral": "0x9c4e1703476e875070ee25b56a58b008cfb8fa78",
    "conditional": "0x69308FB512518e39F9b16112fA8d994F4e2Bf8bB",
}


def mock_salt_generator():
    return salt


class TestOrderBuilder(TestCase):
    def test_validate_order(self):
        builder = OrderBuilder(amoy_contracts["exchange"], chain_id, signer)

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

    def test_validate_order_neg_risk(self):
        builder = OrderBuilder(amoy_contracts["negRiskExchange"], chain_id, signer)

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
        builder = OrderBuilder(amoy_contracts["exchange"], chain_id, signer)

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
            amoy_contracts["exchange"], chain_id, signer, mock_salt_generator
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

    def test_build_order_neg_risk(self):
        builder = OrderBuilder(amoy_contracts["negRiskExchange"], chain_id, signer)

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
            amoy_contracts["negRiskExchange"], chain_id, signer, mock_salt_generator
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

    def test_build_order_signature(self):
        builder = OrderBuilder(
            amoy_contracts["exchange"], chain_id, signer, mock_salt_generator
        )

        _order = builder.build_order(self.generate_data())

        # Ensure struct hash is expected(generated via ethers)
        expected_struct_hash = (
            "0x02ca1d1aa31103804173ad1acd70066cb6c1258a4be6dada055111f9a7ea4e55"
        )
        struct_hash = builder._create_struct_hash(_order)
        self.assertEqual(expected_struct_hash, struct_hash)

        expected_signature = "0x302cd9abd0b5fcaa202a344437ec0b6660da984e24ae9ad915a592a90facf5a51bb8a873cd8d270f070217fea1986531d5eec66f1162a81f66e026db653bf7ce1c"
        sig = builder.build_order_signature(_order)
        self.assertEqual(expected_signature, sig)

    def test_build_order_signature_neg_risk(self):
        builder = OrderBuilder(
            amoy_contracts["negRiskExchange"], chain_id, signer, mock_salt_generator
        )

        _order = builder.build_order(self.generate_data())

        # Ensure struct hash is expected(generated via ethers)
        expected_struct_hash = (
            "0xf15790d3edc4b5aed427b0b543a9206fcf4b1a13dfed016d33bfb313076263b8"
        )
        struct_hash = builder._create_struct_hash(_order)
        self.assertEqual(expected_struct_hash, struct_hash)

        expected_signature = "0x1b3646ef347e5bd144c65bd3357ba19c12c12abaeedae733cf8579bc51a2752c0454c3bc6b236957e393637982c769b8dc0706c0f5c399983d933850afd1cbcd1c"
        sig = builder.build_order_signature(_order)
        self.assertEqual(expected_signature, sig)

    def test_build_signed_order(self):
        builder = OrderBuilder(
            amoy_contracts["exchange"], chain_id, signer, mock_salt_generator
        )

        signed_order = builder.build_signed_order(self.generate_data())

        expected_signature = "0x302cd9abd0b5fcaa202a344437ec0b6660da984e24ae9ad915a592a90facf5a51bb8a873cd8d270f070217fea1986531d5eec66f1162a81f66e026db653bf7ce1c"
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

    def test_build_signed_order_neg_risk(self):
        builder = OrderBuilder(
            amoy_contracts["negRiskExchange"], chain_id, signer, mock_salt_generator
        )

        signed_order = builder.build_signed_order(self.generate_data())

        expected_signature = "0x1b3646ef347e5bd144c65bd3357ba19c12c12abaeedae733cf8579bc51a2752c0454c3bc6b236957e393637982c769b8dc0706c0f5c399983d933850afd1cbcd1c"
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

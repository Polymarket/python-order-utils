from unittest import TestCase, mock
from py_order_utils.builders.exception import ValidationException
from py_order_utils.model.model import LimitOrder, LimitOrderData
from py_order_utils.builders import LimitOrderBuilder
from py_order_utils.model.signatures import EOA


class TestLimitOrderBuilder(TestCase):
    
    def test_validate_order(self):
        lop_builder = LimitOrderBuilder("0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9", 1, mock.MagicMock())

        data = self.generate_data()
        
        # Valid order
        self.assertTrue(lop_builder._validate_inputs(data))

        # Invalid if any of the required fields are missing
        data = self.generate_data()
        data.exchange_address = None
        self.assertFalse(lop_builder._validate_inputs(data))

        # Invalid if the exchange address on the data object is different from the provided contract address
        data = self.generate_data()
        data.exchange_address = "0x0000000000000000000000000000000000000000"
        self.assertFalse(lop_builder._validate_inputs(data))

        # Invalid if both maker_asset_id and taker_asset_id are None
        data = self.generate_data()
        data.maker_asset_id = None
        data.taker_asset_id = None
        self.assertFalse(lop_builder._validate_inputs(data))

    def test_build_limit_order(self):
        lop_builder = LimitOrderBuilder("0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9", 1, mock.MagicMock())

        invalid_data_input = self.generate_data()
        invalid_data_input.exchange_address = "0x0000000000000000000000000000000000000000"
        
        # throw if invalid limit order input
        with self.assertRaises(ValidationException):
            lop_builder.build_limit_order(invalid_data_input)

        limit_order = lop_builder.build_limit_order(self.generate_data())
        
        # Ensure correct values on limit order
        self.assertTrue(isinstance(limit_order["salt"], int))
        
        self.assertEqual("0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512", limit_order["makerAsset"])
        self.assertEqual("0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9", limit_order["takerAsset"])

        self.assertEqual(
            "0x23b872dd00000000000000000000000070997970c51812dc3a010c7d01b50e0d17dc79c8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000f4240", 
            limit_order["makerAssetData"]
        )

        self.assertEqual(
            "0x23b872e1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000070997970c51812dc3a010c7d01b50e0d17dc79c8000000000000000000000000000000000000000000000000000000000007a1200000000000000000000000005fbdb2315678afecb367f032d93f642f64180aa3000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000", 
            limit_order["takerAssetData"]
        )

        self.assertEqual(
            "0xf4a215c300000000000000000000000000000000000000000000000000000000000f4240000000000000000000000000000000000000000000000000000000000007a120",
            limit_order["getMakerAmount"]
        )

        self.assertEqual(
            "0x296637bf00000000000000000000000000000000000000000000000000000000000f4240000000000000000000000000000000000000000000000000000000000007a120",
            limit_order["getTakerAmount"]
        )

        self.assertEqual(
            "0x961d5b1e000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000a00000000000000000000000000000000000000000000000000000000000000002000000000000000000000000cf7ed3acca5a467e9e704c703e8d87f634fb0fc9000000000000000000000000cf7ed3acca5a467e9e704c703e8d87f634fb0fc90000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000000000000000000000000000000000000000002463592c2b0000000000000000000000000000000000000000000000000000000061f5119f000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000044cf6fc6e300000000000000000000000070997970c51812dc3a010c7d01b50e0d17dc79c8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            limit_order["predicate"]
        )
        
        self.assertEqual(
            "0x",
            limit_order["permit"]
        )

        self.assertEqual(
            "0x",
            limit_order["interaction"]
        )

        self.assertEqual(
            "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
            limit_order["signer"]
        )

        self.assertEqual(
            EOA,
            limit_order["sigType"]
        )

    def test_build_signature(self):
        signer = mock.MagicMock()
        expected_signature = "0xf3639d0f921eb0e21ea779394808612a846b6a6ee39c7ed7d369a45bc0b9cdaf00022ec65fff31a2124306d27fc471768f04b1da0ac5e483946a4bf70788dade1b"
        
        # Instead of using a private key, unit tests mock the expected signature response
        signer.sign.return_value = expected_signature
        builder = LimitOrderBuilder("0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9", 31337, signer)
       
        order = LimitOrder(
        salt= 1441990488917,
        makerAsset="0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512",
        takerAsset="0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9",
        makerAssetData="0x23b872dd000000000000000000000000e3d9bfa896af6988f80027bfd13440a42c5ed02b000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000f4240",
        takerAssetData="0x23b872e10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000e3d9bfa896af6988f80027bfd13440a42c5ed02b000000000000000000000000000000000000000000000000000000000007a1200000000000000000000000005fbdb2315678afecb367f032d93f642f64180aa3000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000",
        getMakerAmount='0xf4a215c300000000000000000000000000000000000000000000000000000000000f4240000000000000000000000000000000000000000000000000000000000007a120',
        getTakerAmount='0x296637bf00000000000000000000000000000000000000000000000000000000000f4240000000000000000000000000000000000000000000000000000000000007a120',
        predicate="0x",
        permit="0x",
        interaction="0x",
        signer='0xe3d9BFA896aF6988f80027bfd13440A42C5ed02b',
        sigType=0
        )

        # Ensure struct hash is expected(generated via ethers)
        expected_struct_hash = "0x44b6cebf08a4ebe229ae0c7f5d6f7c7c77f66788e83cf6bba0b6cb9a5dffb3d5"
        struct_hash = builder._create_struct_hash(order)
        self.assertEqual(expected_struct_hash, struct_hash.hex())
        
        sig = builder.build_limit_order_signature(order)
        self.assertEqual(expected_signature, sig)

    def generate_data(self)->LimitOrderData:
        return LimitOrderData(
            salt=990606491137,
            exchange_address="0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9",
            maker_asset_address="0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512",
            taker_asset_address="0x5FbDB2315678afecb367f032d93F642f64180aa3",
            taker_asset_id=1,
            maker_address="0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
            taker_address="0x0000000000000000000000000000000000000000",
            maker_amount=1000000,
            taker_amount=500000,
            expiry=1643450783,
            nonce=0
        )



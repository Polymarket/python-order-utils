from unittest import TestCase, mock
from py_order_utils.model.model import LimitOrderData
from py_order_utils.builders import LimitOrderBuilder


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
        data.exchange_address = "0x"
        self.assertFalse(lop_builder._validate_inputs(data))

        # Invalid if both maker_asset_id and taker_asset_id are None
        data = self.generate_data()
        data.maker_asset_id = None
        data.taker_asset_id = None
        self.assertFalse(lop_builder._validate_inputs(data))

    def test_build_limit_order(self):
        lop_builder = LimitOrderBuilder("0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9", 1, mock.MagicMock())
        
        limit_order = lop_builder.build_limit_order(self.generate_data())
        
        # Ensure correct values on limit order
        self.assertIsNotNone(limit_order.salt)
        
        self.assertEqual("0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512", limit_order.makerAsset)
        self.assertEqual("0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9", limit_order.takerAsset)

        self.assertEqual(
            "0x23b872dd00000000000000000000000070997970c51812dc3a010c7d01b50e0d17dc79c8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000f4240", 
            limit_order.makerAssetData
        )

        self.assertEqual(
            "0x23b872e1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000070997970c51812dc3a010c7d01b50e0d17dc79c8000000000000000000000000000000000000000000000000000000000007a1200000000000000000000000005fbdb2315678afecb367f032d93f642f64180aa3000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000c000000000000000000000000000000000000000000000000000000000000000010000000000000000000000000000000000000000000000000000000000000000", 
            limit_order.takerAssetData
        )

        self.assertEqual(
            "0xf4a215c300000000000000000000000000000000000000000000000000000000000f4240000000000000000000000000000000000000000000000000000000000007a120",
            limit_order.getMakerAmount
        )

        self.assertEqual(
            "0x296637bf00000000000000000000000000000000000000000000000000000000000f4240000000000000000000000000000000000000000000000000000000000007a120",
            limit_order.getTakerAmount
        )

        self.assertEqual(
            "0x961d5b1e000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000a00000000000000000000000000000000000000000000000000000000000000002000000000000000000000000cf7ed3acca5a467e9e704c703e8d87f634fb0fc9000000000000000000000000cf7ed3acca5a467e9e704c703e8d87f634fb0fc90000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000004000000000000000000000000000000000000000000000000000000000000000a0000000000000000000000000000000000000000000000000000000000000002463592c2b0000000000000000000000000000000000000000000000000000000061f5119f000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000044cf6fc6e300000000000000000000000070997970c51812dc3a010c7d01b50e0d17dc79c8000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000",
            limit_order.predicate
        )
        
        self.assertEqual(
            "0x",
            limit_order.permit
        )

        self.assertEqual(
            "0x",
            limit_order.interaction
        )

        self.assertEqual(
            "0x70997970C51812dc3A010C7d01b50e0d17dc79C8",
            limit_order.signer
        )

        self.assertEqual(
            0,
            limit_order.sigType
        )


    def generate_data(self)->LimitOrderData:
        return LimitOrderData(
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



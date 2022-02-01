from unittest import TestCase, mock
from py_order_utils.model.model import MarketOrder, MarketOrderData
from py_order_utils.builders import MarketOrderBuilder
from py_order_utils.model.signatures import EOA
from py_order_utils.signer import Signer


class TestMarketOrderBuilder(TestCase):
    
    def test_validate_inputs(self):
        builder = MarketOrderBuilder("0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9", 31337, mock.MagicMock())

        data = self.generate_data()
        
        # Valid order
        self.assertTrue(builder._validate_inputs(data))

        # Invalid if any of the required fields are missing
        data = self.generate_data()
        data.exchange_address = None
        self.assertFalse(builder._validate_inputs(data))

        # Invalid if the exchange address on the data object is different from the provided contract address
        data = self.generate_data()
        data.exchange_address = "0x0000000000000000000000000000000000000000"
        self.assertFalse(builder._validate_inputs(data))

        # Invalid if both maker_asset_id and taker_asset_id are None
        data = self.generate_data()
        data.maker_asset_id = None
        data.taker_asset_id = None
        self.assertFalse(builder._validate_inputs(data))
        

    def test_build_market_order(self):
        builder = MarketOrderBuilder("0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9", 31337, mock.MagicMock())
        mkt_order = builder.build_market_order(self.generate_data())
        
        # Ensure correct values
        self.assertTrue(isinstance(mkt_order["salt"], int))

        self.assertEqual("0xe3d9BFA896aF6988f80027bfd13440A42C5ed02b", mkt_order["maker"])
        self.assertEqual("0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512", mkt_order["makerAsset"])
        self.assertEqual(1000000, mkt_order["makerAmount"])
        self.assertEqual(0, mkt_order["makerAssetID"])

        self.assertEqual("0x5FbDB2315678afecb367f032d93F642f64180aa3", mkt_order["takerAsset"])
        self.assertEqual(1, mkt_order["takerAssetID"])

        self.assertEqual("0xe3d9BFA896aF6988f80027bfd13440A42C5ed02b", mkt_order["signer"])
        self.assertEqual(EOA, mkt_order["sigType"])

    def test_build_market_order_signature(self):
        expected_sig = "0x88be65ecb593b31977425933df5332f3da1c7b2b54ca033906035dc3d4fd11850e676164e7073e70ef25f881109b39f5b7321df415bc5572d09918c3063669ee1b"
        signer = mock.MagicMock()
        signer.sign.return_value = expected_sig
        
        builder = MarketOrderBuilder("0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9", 31337, signer)
        expected_struct_hash = "0xc568f86a5347e6ace2d4d7eff6215a4669d86ab811be1f9d74ba59717396da90"

        mkt_order = builder.build_market_order(self.generate_data())
        self.assertEqual(expected_struct_hash, builder._create_struct_hash(mkt_order).hex())
        
        signature = builder.build_market_order_signature(mkt_order)
        self.assertEqual(expected_sig, signature)

    def generate_data(self):
        return MarketOrderData(
            salt=284374147907,
            exchange_address="0xCf7Ed3AccA5a467e9e704C703E8D87F634fB0Fc9",
            maker_asset_address="0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512",
            maker_address="0xe3d9BFA896aF6988f80027bfd13440A42C5ed02b",
            maker_asset_id=0,
            maker_amount=1000000,
            taker_asset_address="0x5FbDB2315678afecb367f032d93F642f64180aa3",
            taker_asset_id=1,
        )
    

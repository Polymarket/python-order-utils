from unittest import TestCase, mock
from py_order_utils.builders import LimitOrderBuilder
from py_order_utils.signer import Signer


class TestLimitOrderBuilder(TestCase):
    
    def test_validate_order(self):
        mock_signer = mock.MagicMock()
        lop = LimitOrderBuilder("0x", 1, mock_signer)
        
        pass

    
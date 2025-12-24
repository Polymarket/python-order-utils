from py_order_utils.builders import OrderBuilder, OrderData
from py_order_utils.signer import Signer


class DummySigner(Signer):
    def __init__(self):
        # приватный ключ не важен для структуры, можно любой валидный hex
        super().__init__("0x" + "11" * 32)

    def sign(self, message_hash: bytes) -> bytes:
        # смоук‑тест не проверяет криптографию, только структуру
        return b"\x01" * 65


def test_build_signed_order_smoke():
    exchange_address = "0x" + "aa" * 20
    chain_id = 80002

    signer = DummySigner()
    builder = OrderBuilder(exchange_address, chain_id, signer)

    order = builder.build_signed_order(
        OrderData(
            maker=exchange_address,
            taker="0x" + "bb" * 20,
            token_id="123",
            side="BUY",
            price="0.10",
            size="1.0",
            expiration=9999999999,
            salt="1",
        )
    )

    data = order.dict()

    assert "signature" in data
    assert data["maker"] == exchange_address
    assert data["price"] == "0.10"
    assert data["size"] == "1.0"

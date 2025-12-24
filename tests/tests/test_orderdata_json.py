import json

from py_order_utils.models import OrderData


def test_orderdata_can_be_serialized_to_json() -> None:
    """
    Ensure that OrderData.dict() produces a JSON-serializable payload.
    """
    order = OrderData()

    payload = order.dict()
    serialized = json.dumps(payload)

    assert isinstance(serialized, str)
    assert serialized.startswith("{")

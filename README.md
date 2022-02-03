## python-order-utils

Python utilities used to generate and sign limit and market orders on Polymarket's CLOB


### Install

```bash
pip install py-order-utils
```

### Usage

```py
from py_order_utils.builders import LimitOrderBuilder
from py_order_utils.signer import Signer


exchange_address = "0x...."
chain_id = 1
signer = Signer("0xMockPrivateKey")
builder = LimitOrderBuilder(exchange_address, chain_id, signer)


# Create the limit order
limit_order = builder.build_limit_order(
    LimitOrderData(
        maker_asset_address="0x...",
        taker_asset_address="0x...",
        taker_asset_id=1,
        ...
    )
)

# Sign it
signature = builder.build_limit_order_signature(limit_order)

# Generate the Order and Signature json to be sent to the CLOB
order_and_sig = builder.build_limit_order_and_signature(limit_order, signature).json()

```

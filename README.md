## Polymarket CLOB Python order-utils

<a href='https://pypi.org/project/py-order-utils'>
    <img src='https://img.shields.io/pypi/v/py-order-utils.svg' alt='PyPI'/>
</a>

Python utilities used to generate and sign limit and market orders on Polymarket's CLOB


### Install

```bash
pip install py-order-utils
```

### Usage

```py
from py_order_utils.builders import LimitOrderBuilder
from py_order_utils.signer import Signer
from pprint import pprint

def main():
    exchange_address = "0x...."
    chain_id = 80001
    signer = Signer("0x....")
    builder = LimitOrderBuilder(exchange_address, chain_id, signer)

    # Create and sign the limit order
    limit_order = builder.create_limit_order(
        LimitOrderData(
            maker_asset_address="0x...",
            taker_asset_address="0x...",
            taker_asset_id=1,
            ...
        )
    )

    # Generate the Order and Signature json to be sent to the CLOB API
    pprint(json.dumps(limit_order.dict()))

```

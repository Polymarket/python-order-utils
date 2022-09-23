## Polymarket CLOB Python order-utils

<a href='https://pypi.org/project/py-order-utils'>
    <img src='https://img.shields.io/pypi/v/py-order-utils.svg' alt='PyPI'/>
</a>

Python utilities used to generate and sign orders from Polymarket's Exchange

### Install

```bash
pip install py-order-utils
```

### Usage

```py
from py_order_utils.builders import OrderBuilder
from py_order_utils.signer import Signer
from pprint import pprint

def main():
    exchange_address = "0x...."
    chain_id = 80001
    signer = Signer("0x....")
    builder = OrderBuilder(exchange_address, chain_id, signer)

    # Create and sign the order
    order = builder.build_signed_order(
        OrderData(
            ...
        )
    )

    # Generate the Order and Signature json to be sent to the CLOB API
    pprint(json.dumps(order.dict()))

```

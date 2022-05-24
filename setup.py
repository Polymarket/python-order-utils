import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py_order_utils",
    version="0.0.19",
    author="Jonathan Amenechi",
    author_email="jonathanamenechi@gmail.com",
    description="Python utilities used to generate and sign limit and market orders on Polymarket's CLOB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/polymarket/python-order-utils",
    install_requires=[
        'web3>=5.0.0,<6.0.0',
        'eth-account>=0.4.0,<0.6.0',
        'eip712-structs',
        'pytest',
        'eth-abi',
        'eth_typing',
        'eth_utils',
        'eth_utils',
    ],
    package_data={
        'py_order_utils': [
            'abi/*.json',
        ],
    },
    project_urls={
        "Bug Tracker": "https://github.com/polymarket/python-order-utils",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9.10",
)


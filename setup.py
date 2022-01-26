import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-order-utils",
    version="0.0.1",
    author="Jonathan Amenechi",
    author_email="jonathanamenechi@gmail.com",
    description="Utilities used to generate and sign limit and market orders on Polymarket's CLOB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/polymarket/python-order-utils",
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


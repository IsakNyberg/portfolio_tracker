#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="portfolio_tracker",
    version="0.0.1",
    author="Isak Nyberg",
    description="Tracks basic stats of a stock portfolio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IsakNyberg/portfolio_tracker",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)

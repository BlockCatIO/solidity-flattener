#!python3

from setuptools import setup

setup(
    name='solidity-flattener',
    description='Flattens Solidity code that uses imports into a single file.',
    author='Eric Huang, BlockCAT Technologies Inc.',
    author_email='team@blockcat.io',
    url='https://github.com/BlockCatIO/solidity-flattener',
    version='0.1.1',
    scripts=['src/solidity_flattener']
)
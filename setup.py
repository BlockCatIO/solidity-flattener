#!python3

import sys
if sys.version_info < (3, 5):
    sys.exit('Sorry, Python < 3.5 is not supported')

from setuptools import setup, find_packages

setup(
    name='solidity-flattener',
    description='Flattens Solidity code that uses imports into a single file.',
    author='Eric Huang, BlockCAT Technologies Inc.',
    author_email='team@blockcat.io',
    url='https://github.com/BlockCatIO/solidity-flattener',
    version='0.2.2',
    packages=find_packages(exclude=["*tests"]),
    scripts=['bin/solidity_flattener']
)

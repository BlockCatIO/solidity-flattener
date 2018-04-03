# Solidity Flattener
*A BlockCAT Technologies contribution - https://blockcat.io*

**Are you tired of having to manually combine all of your files** when verifying your contract source on [Etherscan](https://etherscan.io)? This script automatically traverses the dependency graph and outputs all of your imports in the correct order, ready to be pasted into the contract verifier.

This is also useful for quickly throwing your source into [Remix](https://ethereum.github.io/browser-solidity/) without having to fumble with local filesystem connections.

>**NOTE:** This script does not work with imports that are aliased (i.e. `import './A.sol' as B;` ).

# Requirements

* Python 3.5+, `pip`
* `solc`, the [Solidity compiler](http://solidity.readthedocs.io/en/develop/installing-solidity.html#binary-packages)
  * **Note:** The NPM version of the compiler does not expose enough functionality to satisfy the requirements of this tool.

# Installation

`pip3 install solidity-flattener`

# Usage
```
usage: solidity_flattener [-h] [--output FILENAME] [--solc-paths SOLC_PATHS]
                          target_solidity_file

Flattens a target Solidity source file by resolving all of its imports and
dependencies. NOTE: This does not work with imports that are aliased (i.e.
import './A.sol' as B; )

positional arguments:
  target_solidity_file  Specifies the target Solidity source file to flatten.

optional arguments:
  -h, --help            show this help message and exit
  --output FILENAME     Specifies the output destination filename. Outputs to
                        stdout by default.
  --solc-paths SOLC_PATHS
                        Specifies the path replacements to pass onto solidity.
                        See solc --help for more information.
```

# Examples

To flatten a Solidity file:

`solidity_flattener StandardToken.sol`

To output to a file instead of standard out:

`solidity_flattener --output StandardTokenFlattened.sol StandardToken.sol`

To provide [import path redirections](http://solidity.readthedocs.io/en/develop/using-the-compiler.html):

`solidity_flattener --solc-paths="my_solidity_path=my_actual_path" StandardToken.sol`

# Contributions

Pull requests are welcome, or feel free to open an issue to discuss.

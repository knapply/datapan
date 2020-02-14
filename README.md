
# _`datapan`_

<!-- badges: start -->
<!-- [![crates.io](https://img.shields.io/crates/v/datapan.svg)](https://crates.io/crates/datapan) -->
[![Build](https://github.com/knapply/datapan/workflows/Rust+Python/badge.svg)](https://github.com/knapply/datapan/actions)
[![Lifecycle](https://img.shields.io/badge/lifecycle-experimental-orange.svg)]()
<!-- [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) -->
<!-- badges: end -->


# Installation

* get Rust (nightly)

```sh
curl https://sh.rustup.rs -sSf | sh
rustup default nightly
rustc --version # rustc 1.43.0-nightly (58b834344 2020-02-05)
```


* install _`datapan`_

```sh
## create/activate venv
# sudo apt-get install python3-venv
# python3 -m venv datapan_env
# source datapan_env/bin/activate
# python -m pip install --upgrade pip


## install datapan
pip install datapan
```

# Usage

```python
import datapan

some_dir = ""

test = datapan.hello_rust(some_dir)

print(test)
```
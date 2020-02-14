
# _`datapan`_ <a href='https://github.com/knapply/datapan'><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Gold_panning_at_Bonanza_Creek.JPG/318px-Gold_panning_at_Bonanza_Creek.JPG' align="right" /></a>

<!-- badges: start -->
<!-- [![crates.io](https://img.shields.io/crates/v/datapan.svg)](https://crates.io/crates/datapan) -->
[![Build](https://github.com/knapply/datapan/workflows/Rust+Python/badge.svg)](https://github.com/knapply/datapan/actions)
[![Lifecycle](https://img.shields.io/badge/lifecycle-experimental-orange.svg)]()
<!-- [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) -->
<!-- badges: end -->


# Installation


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


# Developer Version

* Rust (nightly)

```sh
curl https://sh.rustup.rs -sSf | sh
# rustup default nightly
rustup update nightly
```

* Poetry

```sh
pip install poetry
```

```sh
make install
make test
```

# _`datapan`_ <a href='https://github.com/knapply/datapan'><img src='https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Gold_panning_at_Bonanza_Creek.JPG/318px-Gold_panning_at_Bonanza_Creek.JPG' align="right" /></a>

<!-- badges: start -->
<!-- [![crates.io](https://img.shields.io/crates/v/datapan.svg)](https://crates.io/crates/datapan) -->
[![Build](https://github.com/knapply/datapan/workflows/Rust+Python/badge.svg)](https://github.com/knapply/datapan/actions)
[![Depends](https://img.shields.io/badge/Depends-Python%3E=3.6-darkgreen.svg)](https://www.python.org/)
[![PyPI](https://badge.fury.io/py/datapan.svg)](https://badge.fury.io/py/datapan)
[![Crates.io](https://img.shields.io/crates/v/datapan.svg)](https://crates.io/crates/datapan)
![stability-experimental](https://img.shields.io/badge/stability-experimental-yellow.svg)
[![Travis-CI Build Status](https://travis-ci.org/knapply/datapan.svg?branch=master)](https://travis-ci.org/knapply/datapan)
[![Codecov test coverage](https://codecov.io/gh/knapply/datapan/branch/master/graph/badge.svg)](https://codecov.io/gh/knapply/datapan?branch=master)
[![PyPI download month](https://img.shields.io/pypi/dm/datapan.svg)](https://pypi.python.org/pypi/datapan/)
<!-- [![crates.io](https://img.shields.io/badge/crates.io-sift-green.svg)](https://crates.io/crates/datapan) -->
<!-- [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) -->
<!-- badges: end -->

<br>

__This is still a worflow test bed. It is not yet useful.__

_`datapan`_ sifts through enormous files in parallelized Rust to only grab the data you want as quickly and memory-efficiently as possilbe.

<br>

# Installation

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
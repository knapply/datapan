
# _`sift`_

<!-- badges: start -->
<!-- [![crates.io](https://img.shields.io/crates/v/sift.svg)](https://crates.io/crates/sift) -->
[![Build](https://github.com/knapply/sift/workflows/Rust+Python/badge.svg)](https://github.com/knapply/sift/actions)
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


* install _`sift`_

```sh
## create/activate venv
# sudo apt-get install python3-venv
# python3 -m venv sift_env
# source sift_env/bin/activate
# python -m pip install --upgrade pip

## install poetry dependency manager
# pip install poetry
# poetry install

## install sift
pip install git+git://github.com/knapply/sift.git
```

# Usage

```python
import sift

some_dir = ""

test = sift.hello_rust(some_dir)

print(test)
```
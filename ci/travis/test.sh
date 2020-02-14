#!/bin/bash
set -ex

if [[ $FEATURES == *"pypy"* ]]; then
    tox -c "tox.ini" -e pypy3
else
    tox -c "tox.ini" -e py
fi

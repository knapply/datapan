#!/bin/bash
set -ex

if [ "$TRAVIS_JOB_NAME" = "Minimum nightly" ]; then
    pip install --pre black==19.3b0
    make lint
fi

if [[ $FEATURES == *"pypy"* ]]; then
    tox -c "tox.ini" -e pypy3
else
    tox -c "tox.ini" -e py


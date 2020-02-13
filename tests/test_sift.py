import os
import pytest
import sift


def get_test_files(target_dir="test-data", target_exts=[".json", ".ndjson"]):
    out = []
    for file in os.listdir(target_dir):
        for ext in target_exts:
            if file.endswith(ext):
                out.append(os.path.join(target_dir, file))
                break
    return out


def test_sift(target_dir="test-data"):
    test = sift.hello_rust(target_dir)
    
    test_files = get_test_files(target_dir)
    target = []
    for file in test_files:
        with open(file) as f:
            for l in f:
                target.append(l)
    
    assert len(test) == len(target)

import os
import sys

from setuptools import setup
from setuptools_rust import Binding, RustExtension
from setuptools.command.test import test as TestCommand
from setuptools.command.sdist import sdist as SdistCommand

from typing import List



class PyTest(TestCommand):
    user_options: List[str] = []

    def run(self):
        self.run_command("test_rust")

        import subprocess

        errno = subprocess.call(["pytest", "tests"])
        raise SystemExit(errno)


# class CargoModifiedSdist(SdistCommand):
#     """Modifies Cargo.toml to use an absolute rather than a relative path
#     The current implementation of PEP 517 in pip always does builds in an
#     isolated temporary directory. This causes problems with the build, because
#     Cargo.toml necessarily refers to the current version of pyo3 by a relative
#     path.
#     Since these sdists are never meant to be used for anything other than
#     tox / pip installs, at sdist build time, we will modify the Cargo.toml
#     in the sdist archive to include an *absolute* path to pyo3.
#     """

#     def make_release_tree(self, base_dir, files):
#         """Stages the files to be included in archives"""
#         super().make_release_tree(base_dir, files)

#         import toml

#         # Cargo.toml is now staged and ready to be modified
#         cargo_loc = os.path.join(base_dir, "Cargo.toml")
#         assert os.path.exists(cargo_loc)

#         with open(cargo_loc, "r") as f:
#             cargo_toml = toml.load(f)

#         rel_pyo3_path = cargo_toml["dependencies"]["pyo3"]["path"]
#         base_path = os.path.dirname(__file__)
#         abs_pyo3_path = os.path.abspath(os.path.join(base_path, rel_pyo3_path))

#         cargo_toml["dependencies"]["pyo3"]["path"] = abs_pyo3_path

#         with open(cargo_loc, "w") as f:
#             toml.dump(cargo_toml, f)




try:
    from setuptools_rust import RustExtension
except ImportError:
    import subprocess

    errno = subprocess.call([sys.executable, "-m", "pip", "install", "setuptools-rust"])
    if errno:
        print("Please install setuptools-rust package")
        raise SystemExit(errno)
    else:
        from setuptools_rust import RustExtension


setup_requires = ["setuptools-rust>=0.10.1", "wheel"]
install_requires: List[str] = []
tests_require = install_requires + ["pytest", "pytest-benchmark"]

setup(name='sift',
      author="Brendan Knapp",
      author_email="brendan.knapp@nps.edu",
      url='http://github.com/knapply/sift/',
      description="sift filters big files.",
      long_description=open("README.md").read(),
      version="0.1.0",
      rust_extensions=[RustExtension('sift', 'Cargo.toml',  binding=Binding.PyO3)],
      test_suite="tests",
      license="MIT",
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities"],
      install_requires=install_requires,
      tests_require=tests_require,
      setup_requires=setup_requires,
      include_package_data=True,
      zip_safe=False,
      cmdclass={"test": PyTest})

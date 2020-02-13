from setuptools import setup
from setuptools_rust import Binding, RustExtension

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
      zip_safe=False)

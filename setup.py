#!/usr/bin/env python
from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)


if __name__ == "__main__":
    setup()
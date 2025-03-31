#!/usr/bin/env python
from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name="text2doc",
    version="0.1.11",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    install_requires=[
        # Add your dependencies here
    ],
)



if __name__ == "__main__":
    setup()
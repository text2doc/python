#!/usr/bin/env python
from setuptools import setup

setup(
    use_scm_version={
        "write_to": "src/text2doc/_version.py",
        "version_scheme": "post-release",
        "local_scheme": "node-and-date",
    },
    setup_requires=["setuptools_scm"],
)


if __name__ == "__main__":
    setup()
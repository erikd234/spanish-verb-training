"""
    Setups to run unit testing.
"""
import setuptools
from setuptools import find_packages


with open("requirements.txt") as f:
    setuptools.setup(
        name="spanish-verb",
        packages=find_packages(exclude=["tests"]),
        install_requires=f.readlines(),
    )

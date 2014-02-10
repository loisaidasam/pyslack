
from distutils.core import setup

setup(
    name="pyslack",
    version="0.1.0",
    description="A Python wrapper for Slack's API",
    author="@LoisaidaSam",
    author_email="sam.sandberg@gmail.com",
    packages=["pyslack"],
    install_requires=["requests"],
)

from distutils.core import setup

from pyslack import __version__


setup(
    name="pyslack",
    version=__version__,
    description="A Python wrapper for Slack's API",
    author="@LoisaidaSam",
    author_email="sam.sandberg@gmail.com",
    packages=["pyslack"],
    install_requires=["requests"],
)

"""The hello command."""

from json import dumps
from pyemojify import emojify
from .base import Base

class Hello(Base):
    """Say hello, world!"""

    def run(self):
        text = emojify("Life is short :smile: , use :sparkles: Python :sparkles:")
        print(text)
        print 'Hello, world!'

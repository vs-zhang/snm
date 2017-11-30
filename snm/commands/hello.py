"""The hello command."""

from pyemojify import emojify
from .base import Base
from ..utils.utils import print_line

class Hello(Base):
    """Say hello, world!"""

    def run(self):
        print_line("Life is short :smile: , use :sparkles: Python :sparkles:")
        print "Hello World!"

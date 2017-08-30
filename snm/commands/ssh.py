"""The ssh command."""

from json import dumps
from .base import Base
import os
from ..utils.utils import find_ips

class SSH(Base):
    """SSH into remote env"""

    def run(self):
        ips = find_ips()
        print 'SSH into some env'
        os.system('ssh {}'.format(ips[0]))

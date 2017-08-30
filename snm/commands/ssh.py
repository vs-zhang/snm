"""The ssh command."""

from json import dumps
from .base import Base
import os
from ..utils.utils import find_ips
import pdb

class SSH(Base):
    """SSH into remote env"""

    def run(self):
        target = self.options['<target>']
        service = self.options['<service>']
        ips = find_ips(target, service)
        print 'SSH into some env'
        print 'ssh {}'.format(ips[0])
        os.system('ssh {}'.format(ips[0]))

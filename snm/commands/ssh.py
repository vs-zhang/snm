"""The ssh command."""

from json import dumps
from .base import Base
import os
from ..utils.utils import find_ips

class SSH(Base):
    """SSH into remote env"""

    def run(self):
        target = self.options['TARGET']
        service = self.options['SERVICE']
        ips = find_ips(target, service)
        print 'SSH into {} {}'.format(target, service)
        print 'ssh {}'.format(ips[0])
        os.system('ssh {}'.format(ips[0]))

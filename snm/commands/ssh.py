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
        host = ips[0]
        print 'The ip of {} {} is {}'.format(target, service, host)
        os.system('ssh -q {}'.format(host))

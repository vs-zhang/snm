"""The ssh command."""

from json import dumps
from .base import Base
import os
from ..utils.utils import find_ips, print_line

class SSH(Base):
    """SSH into remote env"""

    def run(self):
        target = self.options['TARGET']
        service = self.options['SERVICE']
        ips = find_ips(target, service)
        ip = ips[0]
        print_line(':beer:  The IP of {} {} is {} :beer:'.format(target, service, ip))
        os.system('ssh -q {}'.format(ip))

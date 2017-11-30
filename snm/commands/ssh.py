"""The ssh command."""

import os
import inquirer
from json import dumps
from .base import Base
from ..utils.utils import find_ips, print_line

class SSH(Base):
    """SSH into remote env"""

    def run(self):
        target = self.options['TARGET']
        service = self.options['SERVICE']
        is_select_host = self.options['-s']
        ips = find_ips(target, service)
        ip = ips[0]
        if is_select_host:
            questions = [
                inquirer.List('ip',
                    message="Which Host do you want to choose?",
                    choices=ips,
                ),
            ]
            answers = inquirer.prompt(questions)
            ip = answers['ip']
        print_line(':beer:  SSH into {} {}:{} :beer:'.format(target, service, ip))
        os.system("ssh -q -o 'ProxyCommand ssh -q -W %h:%p jump.sessionm.local' {}".format(ip))

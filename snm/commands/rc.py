"""The rails console command."""

from json import dumps
import inquirer
import os
import time
import paramiko
from .base import Base
from ..utils.utils import find_ips, decode_pwd, print_line, get_configs
from ..utils import interactive


class RailsConsole(Base):
    """Rails Console remote env"""
    def run(self):
        target = self.options['TARGET']
        service = self.options['SERVICE']
        is_select_host = self.options['-s']
        configs = get_configs()
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
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        proxy = paramiko.ProxyCommand("ssh -W {}:{} jump.sessionm.local".format(ip, 22))
        # TODO: configure the private key
        # k = paramiko.RSAKey.from_private_key_file("/Users/username/.ssh/id_rsa")
        # ssh.connect(ip, timeout=8, username="username", pkey=k, sock=proxy)
        username = configs.get('username')
        bp = configs.get('bp')
        pwd = decode_pwd(bp)
        ssh.connect(ip, timeout=8, username=username, sock=proxy)
        shell = ssh.invoke_shell()
        shell.send('sudo su - cap\n')
        time.sleep(1)
        shell.send(pwd + "\n")
        time.sleep(1)
        shell.send('cd /product/{}/current\n'.format(service))
        time.sleep(1)
        shell.send('rails c\n')
        time.sleep(1)
        interactive.interactive_shell(shell)
        shell.close()
        ssh.close()

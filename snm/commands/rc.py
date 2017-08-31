"""The rails console command."""

from json import dumps
from .base import Base
import os
import time
import paramiko
from ..utils.utils import find_ips, get_pwd
from ..utils import interactive


class RailsConsole(Base):
    """Rails Console remote env"""

    def run(self):
        target = self.options['TARGET']
        service = self.options['SERVICE']
        ips = find_ips(target, service)
        ip = ips[0]
        print 'SSH into {} {}'.format(target, service)
        print 'ssh {}'.format(ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        k = paramiko.RSAKey.from_private_key_file("/Users/vzhang/.ssh/id_rsa")
        proxy = paramiko.ProxyCommand("ssh -W {}:{} jump.sessionm.local".format(ip, 22))
        ssh.connect(ip, timeout=8, username="vzhang", pkey=k, sock=proxy)
        pwd = get_pwd()
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

"""The rails console command."""

from json import dumps
from .base import Base
import os
import paramiko
from ..utils.utils import find_ips

class RailsConsole(Base):
    """SSH into remote env"""

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
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('ls -al')
        print ssh_stdout.readlines()
        # os.system('ssh {}'.format(ips[0]))

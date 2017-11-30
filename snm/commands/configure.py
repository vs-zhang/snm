"""The configure command."""

import yaml
import inquirer
from pyemojify import emojify
from pprint import pprint
from .base import Base
from ..utils.utils import print_line, encode_pwd, save_configs, get_configs, get_default_configs, get_config_file_path

class Configure(Base):
    """Configure"""

    def run(self):
        print_line(":smile:  Let's configure your profile for the cli.")
        configs = get_configs()
        default_configs = get_default_configs()
        if configs:
            hosts = configs.get('hosts', {})
            services = configs.get('services', {})
        else:
            hosts = default_configs.get('hosts')
            services = default_configs.get('services')

        questions = [
            inquirer.Text('username', message="What's your username"),
            inquirer.Password('pwd', message='Please enter your cap password, {username}'),
            inquirer.Text('xymon_base_url', message="What's xymon's base url", default="http://xymon.infra.local"),
        ]

        answers = inquirer.prompt(questions)
        username = answers.get('username')
        xymon_base_url = answers.get('xymon_base_url')
        pwd = answers.get('pwd')
        bp = encode_pwd(pwd)
        data = {
            'username': username,
            'bp': bp,
            'xymon_base_url': xymon_base_url
        }
        data['hosts'] = hosts
        data['services'] = services
        save_configs(data)

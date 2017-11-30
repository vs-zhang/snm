import requests
import re
import yaml
import os
import base64
from pyemojify import emojify

def print_line(text):
    text = emojify(text)
    print(text)

def remove_duplicates(list):
    result = []
    for item in list:
       if item not in result:
           result.append(item)
    return result

def get_config_file_path():
    main_location = os.getenv('SNM_MAIN', os.path.expanduser('~') + '/.snm')
    if not os.path.isdir(main_location):
        os.makedirs(main_location)
    return main_location + '/config.yml'

def get_default_configs():
    default_config_file_path = os.path.dirname(os.path.realpath(__file__)) + '/config.yml'
    with open(default_config_file_path, 'r') as f:
        return yaml.load(f)

def get_configs():
    config_file_path = get_config_file_path()
    try:
        with open(config_file_path, 'r') as f:
            return yaml.load(f)
    except Exception as error:
        return {}

def save_configs(data):
    config_file_path = get_config_file_path()
    print_line(":tada:  new configure already save to {}".format(config_file_path))
    with open(config_file_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)

def get_url(target, service):
    config = get_configs()
    [env, host] = target.split('.')
    base_url = config['xymon_base_url']
    name = config['hosts'][env]
    service_name = config['services'][service]
    return '{}/xymon/{}/{}-{}/{}/{}.html'.format(base_url, name, host, env, service_name, service_name)

def find_ips(target, service):
    url = get_url(target, service)
    res = requests.get(url)
    return remove_duplicates(re.findall( r'[0-9]+(?:\.[0-9]+){3}', res.content))

def encode_pwd(raw_pwd):
    return base64.b64encode(raw_pwd)

def decode_pwd(encode_pwd):
    return base64.b64decode(encode_pwd)

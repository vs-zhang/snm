import requests
import re
import yaml
import os

def remove_duplicates(list):
    result = []
    for item in list:
       if item not in result:
           result.append(item)
    return result

def get_url(target, service):
    config_file_path = os.path.dirname(os.path.realpath(__file__)) + '/config.yml'
    with open(config_file_path, 'r') as f:
        config = yaml.load(f)
        [env, host] = target.split('.')
        base_url = config['xymon_base_url']
        name = config['hosts'][env]
        return '{}/xymon/{}/{}-{}/{}_v2/{}_v2.html'.format(base_url, name, host, env, service, service)

def find_ips(target, service):
    url = get_url(target, service)
    res = requests.get(url)
    return remove_duplicates(re.findall( r'[0-9]+(?:\.[0-9]+){3}', res.content))
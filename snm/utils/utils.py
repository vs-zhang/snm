import requests
import re

def remove_duplicates(list):
    result = []
    for item in list:
       if item not in result:
           result.append(item)
    return result

def find_ips():
        url = 'http://xymon.infra.local/xymon/enterprise_integration/demo-stg/ondemand_v2/ondemand_v2.html'
        res = requests.get(url)
        return remove_duplicates(re.findall( r'[0-9]+(?:\.[0-9]+){3}', res.content))

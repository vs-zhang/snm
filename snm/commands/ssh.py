"""The hello command."""

from json import dumps
from .base import Base
import requests
import re
import os

class SSH(Base):
    """SSH into"""

    def run(self):
        ips = self.find_ips()
        print 'SSH into some env'
        os.system('ssh {}'.format(ips[0]))

    def remove_duplicates(self, list):
        result = []
        for item in list:
           if item not in result:
               result.append(item)
        return result

    def find_ips(self):
        url = 'http://xymon.infra.local/xymon/enterprise_integration/demo-stg/ondemand_v2/ondemand_v2.html'
        res = requests.get(url)
        return self.remove_duplicates(re.findall( r'[0-9]+(?:\.[0-9]+){3}', res.content))

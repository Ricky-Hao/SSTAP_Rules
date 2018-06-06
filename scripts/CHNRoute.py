import time
import requests
import os

scripts_path = os.path.abspath(__file__)
rules_path = os.path.join(os.path.dirname(os.path.dirname(scripts_path)), 'rules')
file_path = os.path.join(rules_path, 'CHNRoute.rules')
vps_ip = '47.75.42.144/32\n'


header = "=CHNRoute,CHNRoute,1,1,1,0,0,2,{0}\n".format(time.strftime('%Y-%m-%d'))
content = requests.get('http://www.ipdeny.com/ipblocks/data/aggregated/cn-aggregated.zone').text
with open(file_path, 'w+') as f:
    f.write(header+content+vps_ip)

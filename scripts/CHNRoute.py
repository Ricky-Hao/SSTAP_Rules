import time
import requests
import os

scripts_path = os.path.abspath(__file__)
rules_path = os.path.join(os.path.dirname(os.path.dirname(scripts_path)), 'rules')
file_path = os.path.join(rules_path, 'CHNRoute.rules')


header = "=CHNRoute,CHNRoute,1,1,1,0,0,2,{0}\n".format(time.strftime('%Y-%m-%d'))
content = requests.get('http://www.ipdeny.com/ipblocks/data/aggregated/cn-aggregated.zone').text
with open(file_path, 'w+') as f:
    f.write(header+content)

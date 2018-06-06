import time
import requests

header = "=CHNRoute,CHNRoute,1,1,1,0,0,2,{0}\n".format(time.strftime('%Y-%m-%d'))
content = requests.get('http://www.ipdeny.com/ipblocks/data/aggregated/cn-aggregated.zone').text
with open('../rules/CHNRoute.rules', 'w+') as f:
    f.write(header+content)

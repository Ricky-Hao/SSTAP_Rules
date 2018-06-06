import socket
import os
import requests
import time

scripts_path = os.path.abspath(__file__)
rules_path = os.path.join(os.path.dirname(os.path.dirname(scripts_path)), 'rules')
file_path = os.path.join(rules_path, 'Discord.rules')

header = '=Discord,Discord,0,0,1,0,1,2,{0}\n'.format(time.strftime('%Y-%m-%d'))
url = '{0}{1}.discord.gg'
ip_list = []
local_ip = requests.get('http://ipv4.icanhazip.com').text.strip()

for area in ['hongkong', 'japan']:
    for i in range(999):
        try:
            ip = socket.gethostbyname(url.format(area, i))
            if ip != local_ip:
                ip_list.append(ip)
        except socket.gaierror as err:
            pass

with open(file_path, 'w+') as f:
    f.write(header+"/32\n".join(ip_list)+'/32')


        

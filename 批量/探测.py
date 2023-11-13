import os
import requests
from concurrent.futures import ThreadPoolExecutor


 
def http_test(url):
    resp = requests.get(url,timeout=10)
    status = resp.status_code
    if status == 200:
        f.write(url + "\n")
        print(url)

f = open("host.txt", "w")
url = []
for i in range(1, 255):
    url.append("http://192-168-4-" + str(i) + ".pvp3423.bugku.cn")
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(http_test, url)



def ping_test(ip):
    for a in range(1, 20):
        host_ip = ip + str(a)
        result = os.popen(f'ping -n 1 {host_ip}').read()

        # 在ping的输出中查找TTL值，通常TTL值为64表示主机存活
        if "TTL=" in result:
            print(f"{host_ip} is reachable.")
        else:
            print(f"{host_ip} is not reachable.")

ip = '192.168.43.' #网段

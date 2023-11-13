#-- coding:utf-8 --

import requests


def GET_flag(flag_file,method='GET',proxy=None):

    with open(flag_file, 'r', encoding='utf-8') as file:
        flags = file.readlines()

    for flag in flags:
        data_flag = flag.strip()
        payload = {'token': team_token, 'flag': data_flag}

        if method == 'POST':
            try:
                res = requests.post(url, data=payload, headers=headers, proxies=proxy, timeout=3)
                res.raise_for_status()
                print( url,"提交成功!")
            except requests.exceptions.RequestException as err:
                print(url,"提交失败")

        elif method == 'GET':

            try:
                res = requests.get(url, params=payload, headers=headers, proxies=proxy, timeout=3)
                res.raise_for_status()
                print( url,"提交成功!")
            except requests.exceptions.RequestException as err:
                print(url,"提交失败")


def auto_submit_url(url,flagsfile,team_token,method='POST', proxy=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # 打开文件并逐行读取内容
    with open(flagsfile, 'r') as file:
        lines = file.readlines()

    # 创建一个空列表来存储IP地址和逗号后的内容
    data = []

    # 遍历每一行并拆分成IP地址和逗号后的内容
    for line in lines:
        parts = line.strip().split(',')
        if len(parts) == 2:
            ip, flag = parts
            data.append((ip, flag))

    # 提交flag
    for ip, flag in data:
        # print(f'a = {ip}, b = {flag}')
        payload = {'ip':ip,'flag':flag,'token':team_token}
        if method == 'POST':
            try:
                res = requests.post(url, data=payload, headers=headers, proxies=proxy, timeout=3)
                res.raise_for_status()
                print( url,"提交成功!")
            except requests.exceptions.RequestException as err:
                print(url,"提交失败")

        elif method == 'GET':

            try:
                res = requests.get(url, params=payload, headers=headers, proxies=proxy, timeout=3)
                res.raise_for_status()
                print("Success !")
            except requests.exceptions.RequestException as err:
                print(f"Error: {err}")

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# proxy = {'http':'http://127.0.0.1:8080'}

flag_file = 'firstround_flag.txt' #flag文件

method = 'GET' #提交模式

team_token = 'f6bdeb0722892fdae17055a6343af5e3' #token

url = 'https://ctf.bugku.com/pvp/submit.html' #地址


GET_flag(flag_file,method)

# auto_submit_url(url, flag_file, team_token, method=method)



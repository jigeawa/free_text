import requests
import random
import time
from bs4 import BeautifulSoup

print('欢迎使用作文爬取器(v0.9.1)')

i = 0
    
url = input('请输入需要访问的网址: ')
h = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0'}

name = input('请输入保存文件名(后缀加".txt"!): ')

f = open(name, 'w', encoding = 'utf-8')
r = requests.get(url = url, headers = h)
r.encoding = r.apparent_encoding
if r.status_code == 200:
    print('正在读取文件...')
    time.sleep(0.2)
    print('正在解析数据...')
    time.sleep(0.2)
    soup = BeautifulSoup(r.text, 'html.parser')
    print('正在写入数据...(录入需要一点时间，请耐心等待)')
    time.sleep(0.2)
    project = soup.find_all('p')
    print('预计需要时间: ', len(project) * 0.4, '秒\n')
    for j in project:
        f.write(project[i].get_text() + '\n')
        i += 1
        time.sleep(random.uniform(0.3, 0.7))
    f.close()
    input('保存成功! 按回车键退出...')
else:
    print('网站驳回了你的请求')
    print('看看是不是哪里出了问题呢')
    print('错误代码：', r.status_code)
    input('按回车键退出...')
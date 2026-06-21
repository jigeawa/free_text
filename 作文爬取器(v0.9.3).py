import requests
import random
import time
from bs4 import BeautifulSoup

try:
    f = open('date_log.log', 'r', encoding = 'utf-8')
except:
    data_log = 'date_log.log'
    f = open('date_log.log', 'w', encoding = 'utf-8')
    f.write('state,0')

print('欢迎使用作文爬取器(v0.9.3)')
time.sleep(0.2)
if f.read() == 'state,0':
    print('更新日志(仅在第一次运行弹出): ')
    print(' - 新更新了更新日志！这下你可以看到新增功能了！\n - 版本更新为0.9.3\n - 增加了报错信息\n - 改进了0.9.2和0.9.1一直存在的网址'
          '找不到会报错的问题\n - 优化了代码逻辑')
    f.close()
    f = open('date_log.log', 'w', encoding = 'utf-8')
    f.write('state,1')
    f.close()

h = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0'}
my_url = 'https://cruder-recriminatory-ailene.ngrok-free.dev/api/data'

i = 0

def main(): 
    global i, h, my_url
    url = input('请输入需要访问的网址(建议复制粘贴): ')
    name = input('请输入保存文件名(后缀加".txt"!不要使用乱七八糟的字符!): ')

    
    requests.post(url=url, json=url, headers=h)


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
        for _ in project:
            f.write(project[i].get_text() + '\n')
            i += 1
            time.sleep(random.uniform(0.3, 0.7))
        f.close()
        input('保存成功! 按回车键退出...')
    else:
        print('网站驳回了你的请求')
        print('看看是不是哪里出了问题呢')
        print('错误代码(网站返回)：', r.status_code)
        print('尝试解决方法:\n1.检查网络连接\n2.检查网址是否存在拼写错误\n3.检查网站是否被封禁')
        print('若按上述做法尝试后问题仍无法解决 请联系开发者--jigeawa@outlook.com')
        input('按回车键退出...')

try:
    main()
except Exception as e:
    time.sleep(0.3)
    print('程序运行时出错')
    print('错误信息: ', e)
    print('尝试解决方法:\n1.检查网络连接\n2.检查网址是否存在拼写错误\n3.检查网站是否被封禁')
    print('若按上述做法尝试后问题仍无法解决 请联系开发者--jigeawa@outlook.com')
    input('按回车键退出...')
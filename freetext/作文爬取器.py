from tkinter import messagebox
import requests
import tkinter as tk
import random
import time
from bs4 import BeautifulSoup as soup
print('库已导入')
time.sleep(0.2)

h = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0'}
now_version = '0.9.4'
print('正在检查版本...')
try:
    benurl = 'https://jigeawa.dpdns.org/api/catch_free_text'
    r = requests.get(url=benurl, headers=h)
    r.encoding = r.apparent_encoding
    if r.status_code == 200:
        print('now_version: ' + r.text)
        if r.text.strip() != now_version:
            messagebox.showwarning('版本过旧', '当前版本过旧, 推荐前往GitHub下载最新版本, \n\n'
                                        '下载地址:https://github.com/jigeawa/free_text')
        else:
            print('你已是最新版本')
except Exception as e:
    print('检查失败')
    print(e)

print('版本检查结束')
time.sleep(0.2)
print('程序启动中...')

def main(ur, na):
    global h
    i = 0
    url = ur
    name = na + '.txt'
    f = open(name, 'w', encoding='utf-8')

    r = requests.get(url=url, headers=h)
    r.encoding = r.apparent_encoding

    if r.status_code == 200:
        messagebox.showinfo('步骤1: ', '正在写入数据...(录入需要一点时间，请耐心等待)')
        time.sleep(0.2)
        html_soup = soup(r.text, 'html.parser')
        project = html_soup.find_all('p')
        messagebox.showinfo('步骤2: ', f'预计需要时间: {len(project) * 0.4} 秒 (期间程序可能造成未响应 属于正常现象)\n')
        with open(name, 'w', encoding='utf-8') as f:
            for p in project:
                f.write(p.get_text() + '\n')
                time.sleep(random.uniform(0.3, 0.7))
        messagebox.showinfo('完成', '爬取并保存完成！')
    else:
        messagebox.showerror('请求失败', f'网站驳回了你的请求\n错误代码: {r.status_code}\n\n'
                                         '请检查：\n1. 网络连接\n2. 网址拼写\n3. 网站是否被封禁\n'
                                         '若问题依旧，请联系开发者 -- jigeawa@outlook.com')
        print('请关闭弹窗后退出程序')
time.sleep(0.1)
print('主函数定义完毕')
time.sleep(0.2)
print('正在创建界面...')
win = tk.Tk()
win.title('作文爬取器')
win.geometry('600x600')
time.sleep(0.2)
print('启动成功! ')

please_ask = tk.Label(win, text='请输入需要访问的网址(建议复制粘贴): ')
please_ask.pack()

entry_u = tk.Entry(win, width=50, bd=6)
entry_u.pack()

please_ask2 = tk.Label(win, text='请输入保存文件名(不要使用乱七八糟的字符!): ')
please_ask2.pack()

entry_n = tk.Entry(win, width=50, bd=6)
entry_n.pack()

def start():
    url = entry_u.get().strip()
    filename = entry_n.get().strip()
    if not url or not filename:
        messagebox.showwarning("提示", "请输入网址和文件名！")
        return
    main(url, filename)

btn = tk.Button(win, text='开始爬取', command=start)
btn.pack()

win.mainloop()
print('程序关闭')
# 建立属于自己的开放代理IP池
import requests
import random
import time
from lxml import etree
import re
import json

def extract_fps_list(s):
    # 1. 查找 "const fpsList"
    start_idx = s.find("const fpsList")
    if start_idx == -1:
        return None
    
    # 2. 找到第一个 '['
    left_bracket_idx = s.find('[', start_idx)
    if left_bracket_idx == -1:
        return None
    
    # 3. 匹配对应的 ']'（处理嵌套括号）
    count = 1
    current_idx = left_bracket_idx + 1
    n = len(s)
    while current_idx < n and count > 0:
        if s[current_idx] == '[':
            count += 1
        elif s[current_idx] == ']':
            count -= 1
        current_idx += 1
    
    if count != 0:  # 括号不匹配
        return None
    
    # 4. 提取括号内的内容
    right_bracket_idx = current_idx - 1
    content = s[left_bracket_idx :right_bracket_idx+1].strip()
    
    return json.loads(content)

class IpPool:
    def __init__(self):
        # 测试ip是否可用url
        self.test_url = 'http://httpbin.org/get'

        # 获取IP的 目标url
        self.url = 'https://www.89ip.cn/index_{}.html'
        # 高匿代理
        self.url = 'https://www.kuaidaili.com/free/inha/{}/'
        #self.url = 'https://www.kuaidaili.com/free/intr/{}/'

        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'}
        # 存储可用ip
        self.file = r'ip_pool.txt'
    def get_html(self, url):
        '''获取页面'''
        html = requests.get(url=url, headers=self.headers).text

        return html

    def get_proxy(self, url):
        '''数据处理  获取ip 和端口''' 
        html = self.get_html(url=url)
        #print(html)
       
        elemt = etree.HTML(html)
        
        #89ip 
        ips_list = elemt.xpath('//table/tbody/tr/td[1]/text()')
        ports_list = elemt.xpath('//table/tbody/tr/td[2]/text()')

        #kuaidaili
        all_list=extract_fps_list(html)
        ips_list = [item['ip'] for item in all_list]  # 提取所有IP
        ports_list = [item['port'] for item in all_list]  # 提取所有端口


        for ip, port in zip(ips_list, ports_list):
            # 拼接ip与port
            proxy = ip.strip() + ":" + port.strip()
            # print(proxy)
            
            # 175.44.109.195:9999
            self.test_proxy(proxy)

    def test_proxy(self, proxy):
        '''测试代理IP是否可用'''
        proxies = {
            'http': 'http://{}'.format(proxy),
            'https': 'https://{}'.format(proxy),
        }
        # 参数类型
        # proxies
        # proxies = {'协议': '协议://IP:端口号'}
        # timeout 超时设置 网页响应时间3秒 超过时间会抛出异常
        try:
            resp = requests.get(url=self.test_url, proxies=proxies, headers=self.headers, timeout=.8)
           # 获取 状态码为200 
            if resp.status_code == 200:
                print(proxy, '可用')
                # 可以的IP 写入文本以便后续使用
                with open(self.file, 'a', encoding='utf-8') as file:
                    file.write(proxy+'\n')
                
                
            else:
                print(proxy, '不可用')

        except Exception as e:
            print(proxy, '不可用')

    def crawl(self):
        '''执行函数'''
        # 快代理每页url 的区别
        # https://www.kuaidaili.com/free/inha/1/
        # https://www.kuaidaili.com/free/inha/2/
        # .......
        # 提供的免费ip太多
        # 这里只获取前100页提供的免费代理IP测试
        for i in range(1, 101):
            # 拼接完整的url
            page_url = self.url.format(i)
            print(page_url)
            # 注意抓取控制频率
            #time.sleep(random.randint(1, 4))
            time.sleep(random.random()*2)
            self.get_proxy(url=page_url)

if __name__ == '__main__':
    ip = IpPool()
    ip.crawl()
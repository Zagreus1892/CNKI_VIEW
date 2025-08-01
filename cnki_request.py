import requests
from bs4 import BeautifulSoup
import time
import random
import re
import pandas as pd
from dateutil import parser

def normalize_date(date_str):
    try:
        # 预处理：替换全角冒号，提取日期部分
        processed = date_str.replace('：', ':').strip()
        date_part = processed.split()[0]  # 分割空格前的日期部分
        # 解析日期，优先年在前
        dt = parser.parse(date_part, yearfirst=True, fuzzy=True)
        return dt.strftime("%Y-%m-%d")
    except:
        return None  # 解析失败返回None，可自定义处理错误

def try_getText(x):
    try:
        text = x.get_text(strip=True)
        return text
    except:
        return None


def re_getBs(retext, alltext):
    match = re.search(retext, alltext)
    if match:
        inf = match.group(0)
        # print(inf)
        bs = BeautifulSoup(inf, "html.parser")
        return bs
    else:
        return BeautifulSoup()


def cnki_crawler(keyword, choose_max_page=3, kind='all', abstr_need=False):
    brief_mess = []
    extra_mess = []

    # 基础URL（需根据实际分析结果替换为真实接口）
    session = requests.Session()
    base_url = r"https://kns.cnki.net/kns8s/brief/grid"
    headers = {
        'Accept': '*/*',
        'Accept-encoding': 'gzip, deflate, br, zstd',
        'Accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://kns.cnki.net',
        'Referer': 'https://kns.cnki.net/kns8s/defaultresult/index?crossids=YSTT4HG0,LSTPFY1C,JUP3MUPD,MPMFIG1A,WQ0UVIAA,BLZOG7CK,PWFIRAGL,EMRPGLPA,NLBO1Z6R,NN3FJMUV&korder=SU&kw=%E9%98%BF%E6%96%AF%E9%A1%BF',
        'Sec-ch-ua': '"Microsoft Edge";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'
        #'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'    
    }
    data = {'BoolSearch': 'true', 'PageSize': '50'}

    max_page = choose_max_page
    page = 1
    ip_num=0

    with open('ip_pool.txt', 'r') as f:
        ip_pool = f.readlines()
    ips = [line.strip() for line in ip_pool]  # 使用strip去除每行两端的空白字符（包括换行符）

    # ip池
    # proxies = {'协议': '协议://IP:端口号'}
    proxies = {
                'http': 'http://{}'.format(ips[ip_num])
            }
    print('使用代理ip：{}'.format(ips[ip_num]))

    while page <= max_page:
        # data={
        # 'BoolSearch': 'true',
        # CROSSDB WD0FTY92 全部 JOURNAL
        # 'QueryJson': '{"Platform":"","Resource":"CROSSDB","Classid":"WD0FTY92","Products":"","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":0,"Items":[{"Field":"SU","Value":"'+keyword+'","Operator":"TOPRANK","Logic":0,"Title":"主题"}],"ChildItems":[]}]},"ExScope":1,"SearchType":2,"Rlang":"CHINESE","KuaKuCode":"YSTT4HG0,LSTPFY1C,JUP3MUPD,MPMFIG1A,WQ0UVIAA,BLZOG7CK,PWFIRAGL,EMRPGLPA,NLBO1Z6R,NN3FJMUV","Expands":{},"SearchFrom":1}',
        # 'QueryJson': '{"Platform":"","Resource":"JOURNAL","Classid":"YSTT4HG0","Products":"CJFQ,CAPJ,CJTL,CDFD,CMFD,CPFD,IPFD,CPVD,CCND,SCSF,SCHF,SCSD,SNAD,CCJD,WBFD,CCVD,CJFN","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":0,"Items":[{"Field":"SU","Value":"'+keyword+'","Operator":"TOPRANK","Logic":0,"Title":"主题"}],"ChildItems":[]}]},"ExScope":1,"SearchType":2,"Rlang":"CHINESE","KuaKuCode":"","Expands":{},"SearchFrom":11}'
        # 'PageNum': '1',
        # 'PageSize': '50',
        # 'Dstyle': 'listmode',
        # 'ProductStr': 'YSTT4HG0,LSTPFY1C,RMJLXHZ3,JQIRZIYA,JUP3MUPD,1UR4K4HZ,BPBAFJ5S,R79MZMCB,MPMFIG1A,WQ0UVIAA,NB3BWEHK,XVLO76FD,HR1YT1Z9,BLZOG7CK,PWFIRAGL,EMRPGLPA,J708GVCE,ML4DRIDX,NLBO1Z6R,NN3FJMUV,',
        # 'Aside': '主题：浮游植物',
        # 'SearchFrom': '资源范围：总库',
        # 'CurPage': '1',
        # 'Host':'kns.cnki.net'
        # }
        # 翻页
        data['PageNum'] = str(page)
        # 文献类型
        if kind == 'all':
            data['QueryJson'] = '{"Platform":"","Resource":"CROSSDB","Classid":"WD0FTY92","Products":"","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":0,"Items":[{"Field":"SU","Value":"'+keyword + \
                '","Operator":"TOPRANK","Logic":0,"Title":"主题"}],"ChildItems":[]}]},"ExScope":1,"SearchType":2,"Rlang":"CHINESE","KuaKuCode":"YSTT4HG0,LSTPFY1C,JUP3MUPD,MPMFIG1A,WQ0UVIAA,BLZOG7CK,PWFIRAGL,EMRPGLPA,NLBO1Z6R,NN3FJMUV","Expands":{},"SearchFrom":1}'
        elif kind == '期刊':
            data['QueryJson'] = '{"Platform":"","Resource":"JOURNAL","Classid":"YSTT4HG0","Products":"CJFQ,CAPJ,CJTL,CDFD,CMFD,CPFD,IPFD,CPVD,CCND,SCSF,SCHF,SCSD,SNAD,CCJD,WBFD,CCVD,CJFN","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":0,"Items":[{"Field":"SU","Value":"' + \
                keyword + \
                '","Operator":"TOPRANK","Logic":0,"Title":"主题"}],"ChildItems":[]}]},"ExScope":1,"SearchType":2,"Rlang":"CHINESE","KuaKuCode":"","Expands":{},"SearchFrom":11}'
        elif kind == '学术论文':
            data['QueryJson'] = '{"Platform":"","Resource":"DISSERTATION","Classid":"LSTPFY1C","Products":"CJFQ,CAPJ,CJTL","QNode":{"QGroup":[{"Key":"Subject","Title":"","Logic":0,"Items":[{"Field":"SU","Value":"' + \
                keyword + \
                '","Operator":"TOPRANK","Logic":0,"Title":"主题"}],"ChildItems":[]}]},"ExScope":1,"SearchType":2,"Rlang":"CHINESE","KuaKuCode":"","Expands":{},"SearchFrom":11}'
        else:
            raise "文献类型搞错了"

        try:
            if page > 1:
                print(f"预计爬取 {max_page} 页，当前是第 {page} 页")
                data['QueryJson'] = data['QueryJson'].replace(
                    '"SearchFrom":11', '"SearchFrom":4')
                data['QueryJson'] = data['QueryJson'].replace(
                    '"SearchFrom":1', '"SearchFrom":4')
                data['BoolSearch'] = 'false'

            response = session.post(base_url, data=data, headers=headers, proxies=proxies,timeout=5)
            response.encoding = 'utf-8'
            #response.encoding = 'gbk'
            #print(response.text)
            response.raise_for_status()  # 检查HTTP错误
            

            # 假设返回HTML（若为JSON则直接解析）
            soup = BeautifulSoup(response.text, 'html.parser')
            #print(soup)
            if page == 1:
                total_num = try_getText(soup.find('em'))
                total_num = int(total_num.replace(',', ''))
                print(f"总计 {total_num} 篇文献")
                real_max_page = total_num // 50 + 1
                if max_page < real_max_page:
                    pass
                else:
                    max_page = real_max_page
                print(f"预计爬取 {max_page} 页，当前是第 {page} 页")

            brief_infs = soup.select('tr')
            brief_infs = brief_infs[1:]
            # print(brief_infs[0])

            if brief_infs:
                for brief_inf in brief_infs:
                    # 提取文本并合并内部标签内容
                    print('-'*50)
                    t_inform = brief_inf.find('a', class_='fz14')
                    title = try_getText(t_inform)
                    title_url = t_inform.get('href')

                    date = try_getText(brief_inf.find(class_='date'))
                    #date = date[:11]
                    date = normalize_date(date)

                    authorlist_bs = brief_inf.find(class_='author')
                    authors = try_getText(authorlist_bs)
                    authorlist = authorlist_bs.select('a')
                    authors = ''
                    for a in authorlist:
                        authors += a.get_text()
                        authors += '、'
                    authors = authors[:-1]

                    first_author = try_getText(
                        authorlist_bs.find('a'))
                    if first_author:
                        pass
                    else:
                        first_author=authors

                    s_inform = brief_inf.find(class_='source')
                    s_inform = s_inform.find('a')
                    if kind == 'all':
                        source = try_getText(s_inform)
                        liter_type = try_getText(brief_inf.find('span'))
                    elif kind == '学术论文':
                        source = try_getText(brief_inf.find(class_='unit'))
                        liter_type = try_getText(brief_inf.find(class_='data'))
                        first_author = try_getText(
                            brief_inf.find(class_='author'))
                        authors = first_author
                    else:
                        source = try_getText(brief_inf.find('span'))
                        liter_type = kind

                    if s_inform:
                        source_url = s_inform.get('href')
                    else:
                        source_url = None

                    print(date, liter_type, source)
                    print(first_author, title)

                    # 文献类型 题名 第一作者 来源 发表时间 文章链接 来源链接 所有作者
                    brief_mess.append(
                        [liter_type, title, first_author, source, date, title_url, source_url, authors])
                    if abstr_need == True:
                        # 摘要页面
                        #time.sleep(0.5+random.random())  # 避免高频请求
                        # print('-'*40)
                        print(title_url)
                        headers1 = {
                            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0',
                            'Cookie': 'cangjieStatus_NZKPT2=true; cangjieConfig_NZKPT2=%7B%22status%22%3Atrue%2C%22startTime%22%3A%222022-10-20%22%2C%22endTime%22%3A%222025-04-24%22%2C%22orginHosts%22%3A%22kns.cnki.net%22%2C%22type%22%3A%22mix%22%2C%22poolSize%22%3A%2210%22%2C%22intervalTime%22%3A10000%2C%22persist%22%3Afalse%7D; Ecp_notFirstLogin=6quFXs; Ecp_ClientId=i241101140100549940; Ecp_loginuserbk=xn0165; Ecp_ClientIp=112.18.13.254; UM_distinctid=1949715c9edcf0-08bffd248f1ab7-4c657b58-144000-1949715c9ee1955; Hm_lvt_dcec09ba2227fd02c55623c1bb82776a=1736863356,1737037021,1737701412,1739004671; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221930f5885ba755-0c2a35cc72e6c98-4c657b58-1327104-1930f5885bb1a3d%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%221930f5885ba755-0c2a35cc72e6c98-4c657b58-1327104-1930f5885bb1a3d%22%7D; cnkiUserKey=57dde13b-593c-19f9-7f4c-9f9b821a2ce1; _c_WBKFRo=UkBUAAZOAJniLY0GQsVBMLdZVM6d6iTR5MrnJKi9; Ecp_notFirstLogin=I62AWI; knsadv-searchtype=%7B%22BLZOG7CK%22%3A%22gradeSearch%2CmajorSearch%22%2C%22MPMFIG1A%22%3A%22gradeSearch%2CmajorSearch%2CsentenceSearch%22%2C%22T2VC03OH%22%3A%22gradeSearch%2CmajorSearch%22%2C%22JQIRZIYA%22%3A%22gradeSearch%2CmajorSearch%2CsentenceSearch%22%2C%22S81HNSV3%22%3A%22gradeSearch%22%2C%22YSTT4HG0%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22ML4DRIDX%22%3A%22gradeSearch%2CmajorSearch%22%2C%22WQ0UVIAA%22%3A%22gradeSearch%2CmajorSearch%22%2C%22VUDIXAIY%22%3A%22gradeSearch%2CmajorSearch%22%2C%22NN3FJMUV%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22LSTPFY1C%22%3A%22gradeSearch%2CmajorSearch%2CsentenceSearch%22%2C%22HHCPM1F8%22%3A%22gradeSearch%2CmajorSearch%22%2C%22OORPU5FE%22%3A%22gradeSearch%2CmajorSearch%22%2C%22WD0FTY92%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22BPBAFJ5S%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22EMRPGLPA%22%3A%22gradeSearch%2CmajorSearch%22%2C%22PWFIRAGL%22%3A%22gradeSearch%2CmajorSearch%2CsentenceSearch%22%2C%22U8J8LYLV%22%3A%22gradeSearch%2CmajorSearch%22%2C%22R79MZMCB%22%3A%22gradeSearch%22%2C%22J708GVCE%22%3A%22gradeSearch%2CmajorSearch%22%2C%22HR1YT1Z9%22%3A%22gradeSearch%2CmajorSearch%22%2C%22JUP3MUPD%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22NLBO1Z6R%22%3A%22gradeSearch%2CmajorSearch%22%2C%22RMJLXHZ3%22%3A%22gradeSearch%2CmajorSearch%2CsentenceSearch%22%2C%221UR4K4HZ%22%3A%22gradeSearch%2CmajorSearch%2CauthorSearch%2CsentenceSearch%22%2C%22NB3BWEHK%22%3A%22gradeSearch%2CmajorSearch%22%2C%22XVLO76FD%22%3A%22gradeSearch%2CmajorSearch%22%7D; createtime-advInput=2025-04-13%2021%3A51%3A29; SID_kns_new=kns2618132; LID=WEEvREcwSlJHSldSdmVpZ0doOFdTQ1F6WUtqcER5aXFzV2c0cGt2N0hzbz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!; Ecp_session=1; Ecp_LoginStuts={"IsAutoLogin":false,"UserName":"xn0165","ShowName":"%E5%9B%9B%E5%B7%9D%E5%86%9C%E4%B8%9A%E5%A4%A7%E5%AD%A6","UserType":"bk","BUserName":"","BShowName":"","BUserType":"","r":"6quFXs","Members":[]}; SID_restapi=018131; c_m_LinID=LinID=WEEvREcwSlJHSldSdmVpZ0doOFdTQ1F6WUtqcER5aXFzV2c0cGt2N0hzbz0=$9A4hF_YAuvQ5obgVAqNKPCYcEjKensW4IQMovwHtwkF4VYPoHbKxJw!!&ot=04%2F14%2F2025%2015%3A07%3A14; c_m_expire=2025-04-14%2015%3A07%3A14; tfstk=gbUxhgmSKTXm7duhoZskjYi1sWflqPFVe-PBSADDf8e8h8YmftPGBNH8EoYil-DTW5GihsoiINHTUJHfgGkm1cwgQF2T_slsCRwtIojl-SPq7V6nBwb3gfvDRiUx5dVSufVRgUuA-SP2NV571A7HBr1ibRM_Cm9SPXDS1fi_CUGSUfl6hfTfw7MrFnGsCcGWVfc9GVg_C71-_YGjpydxIIM9WkPont8kHx865zhxcgVjFFGzyjnxdSav5FOEMmHQGY6F7A7KV5oT7C8thSZUQXwXh9m41ue-MVQkc2N8fJhzlwvxaoV7tYNp_FPqkkUKloBy4q2YP4abvCT_wqHqXzmJHTHQu7aEP0bC97aznSz8sC_sZJD7grgOR6uxlxg-aPXylAE7frmq7K6n05Z8ej3C4Xz3J9BBKvhMc_CJbhoja1Pz42QiBlJ-wvfkqh-Zqbl-K_CJbhojabHhZaxwb0cP.'
                        }
                        abstr_response = requests.get(
                            title_url, headers=headers1, timeout=10)
                        abstract_bs = BeautifulSoup(
                            abstr_response.text, "html.parser")  # 解析文档，用html的解析器
                        abstract = try_getText(abstract_bs.find(
                            'span', class_='abstract-text'))
                        keywords = try_getText(
                            abstract_bs.find('p', class_='keywords'))
                        DOI = try_getText(
                            re_getBs(r'DOI：.*?</li>', abstr_response.text).find('p'))
                        master = try_getText(
                            re_getBs(r'导师：.*?</p>', abstr_response.text).find('p'))

                        # print(abstract)
                        print(keywords)
                        print(DOI)
                        print(master)
                        # 摘要 关键词 DOI 导师
                        extra_mess.append([abstract, keywords, DOI, master])
                    else:
                        extra_mess.append([None, None, None, None])

            else:
                print("未找到class='name'的单元格")
                if ip_num < len(ips)-1:
                    ip_num+=1
                    proxies = {
                            'http': 'http://{}'.format(ips[ip_num])
                            }
                    print('更改代理ip为：{}'.format(ips[ip_num]))
                else:
                    page+=1
                continue
            print('-'*50)
            
            #time.sleep(0.5+random.random())  # 避免高频请求

        except requests.exceptions.RequestException as e:
            print(f"请求失败: {e}")
            if ip_num < len(ips)-1:
                ip_num+=1
                proxies = {
                        'http': 'http://{}'.format(ips[ip_num])
                        }
                print('更改代理ip为：{}'.format(ips[ip_num]))
                page -= 1
            else:
                break
            #max_page=0
        page += 1
    bdf = pd.DataFrame(brief_mess, columns=['类型', '标题', '第一作者', '来源', '日期', '链接', '来源链接', '所有作者'])
    edf = pd.DataFrame(extra_mess, columns=['摘要' ,'关键词' ,'DOI' ,'导师'])
    df = pd.merge(bdf,edf,left_index=True, right_index=True)
    print(bdf)
    print(edf)
    for i in df.columns:
        df[i]=df[i].str.replace(r'[\ue000-\uf8ff]', '', regex=True)
    #df.to_csv(f'CNKI_{keyword}.csv',encoding='gbk',index=True,index_label='序号')
    df.to_csv(f'CNKI_{keyword}.tsv',encoding='gbk',index=True, sep='\t',index_label='序号')


if __name__ == "__main__":
    pd.set_option('display.encoding', 'gbk') 
    keyword = "卷积神经网络"
    cnki_crawler(keyword, 20, 'all', True)
    # 主题 最大页码数 文献类型 需要摘要

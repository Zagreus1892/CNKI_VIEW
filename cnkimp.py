import time
import random
import os
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from urllib.parse import urljoin
import multiprocessing as mp
from multiprocessing import Process


def webserver():
    # get直接返回，不再等待界面加载完成
   
    desired_capabilities = DesiredCapabilities.EDGE
    desired_capabilities["pageLoadStrategy"] = "none"

    # 设置微软驱动器的环境

    options = webdriver.EdgeOptions()
    
    options.add_argument('--headless')
    #options.add_argument('--disable-gpu')
    # 设置chrome不加载图片，提高速度
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

    # 创建一个微软驱动器
    driver = webdriver.Edge(options=options)
    #driver.minimize_window()

    # 设置所需篇数
    '''
    desired_capabilities = DesiredCapabilities.FIREFOX
    desired_capabilities["pageLoadStrategy"] = "none"
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Firefox(options=options)
    '''
    
    return driver

def open_page(driver, theme):
    # 打开页面
    ran=random.random()+0.1
    driver.get("https://kns.cnki.net/kns8/AdvSearch")
    time.sleep(ran)

    # 传入关键字
    WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="gradetxt"]/dd[1]/div[2]/input'))).send_keys(theme)
    time.sleep(ran+0.2)
    # 关闭纱栾知网的复选框
    WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ModuleSearch"]/div[1]/div/div[2]/ul/li[5]'))).click()
    
    time.sleep(ran)
    
    # 点击搜索
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div[3]/input"))).click()
    time.sleep(ran)
    
    #切换到50篇文献一页
    time.sleep(1)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/div/div/span'))).click()
    time.sleep(0.5)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]/div[2]/div/div/ul/li[3]/a'))).click()
    time.sleep(0.5)

    # 点击切换中文文献
   # WebDriverWait(driver, 100).until(
        #EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[1]/div/div/div/a[1]"))).click()
    #time.sleep(0.3)

    # 跳转到第三页
    # WebDriverWait(driver, 100).until(
    #     EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[2]/form/div/div[2]/a[2]"))).click()
    # time.sleep(3)
    return driver

    

def how_much_paper(driver):
    # 获取总文献数和页数
    res_unm = WebDriverWait(driver, 100).until(EC.presence_of_element_located(
        (By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/div/div/a/em"))).text

    # 去除千分位里的逗号
    res_unm = res_unm.replace(",", '')
    res_unm = res_unm.replace(".", '')
    res_unm = int(res_unm.replace("万", '00'))
    page_unm = int(res_unm / 50) + 1
    print(f"共找到 {res_unm} 条结果, {page_unm} 页。")
    return res_unm

def crawl(shared_list,papers_need, theme ,duandian,num=1):
    
    ran=random.random()+0.1
    # 赋值序号, 控制爬取的文章数量
    driver = webserver()
    count = 1
    error = 0
    print('进程 {} 开始运行'.format(num))
    namer=theme.replace('\"','\'')
    namer=namer.replace('*','_')

    driver= open_page(driver,theme)

    wxnum=1
    count+=duandian
    papers_need+=duandian
    turn=duandian//50
    if turn>=8:
        time.sleep(1)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[2]/div[9]"))).click()
        turn-=8
    for i in range(turn):
        time.sleep(4)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@id='PageNext']"))).click()
        
    
    # 当爬取数量小于需求时，循环网页页码
    while count <= papers_need:
        # 等待加载完全，休眠3S
        time.sleep(2)

        
        title_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fz14")))
        #print(title_list)
        net=[]
        for i in title_list:
            #print(i.get_attribute("href"))
            net.append(i.get_attribute("href"))
        #print(net)


        # 循环网页一页中的条目
        for i in range(duandian%50,len(title_list)):
            if count > papers_need:
                break
            try:
                if count % 50 != 0:
                    term = count % 50  # 本页的第几个条目
                else:
                    term = 50
                    time.sleep(2)

                title_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/table/tbody/tr[{term}]/td[2]"
                author_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/table/tbody/tr[{term}]/td[3]"
                source_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/table/tbody/tr[{term}]/td[4]"
                date_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/table/tbody/tr[{term}]/td[5]"
                database_xpath = f"/html/body/div[2]/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div/table/tbody/tr[{term}]/td[6]"
                title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, title_xpath))).text
                #authors = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, author_xpath))).text
                source = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, source_xpath))).text
                date = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, date_xpath))).text
                database = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, database_xpath))).text
                #print(database)
                if database!='期刊' and  database!='硕士' and database!='博士':#只要这几种 看看有没有in写法
                    continue
                # 点击条目
                #driver.get(net[i]) 这个是覆盖
                '''
                url=net[i]
                js_code = f'window.open("{url}");' # 构造JavaScript代码 打开新标签页
                driver.execute_script(js_code) # 执行JavaScript代码
                '''
                title_list[i].click() 
                
                # 获取driver的句柄
                n = driver.window_handles
                # driver切换至最新生产的页面
                driver.switch_to.window(n[-1])
                #driver.minimize_window()
                time.sleep(ran)
                # 开始获取页面信息
                #展开
                try:
                    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ChDivSummaryMore']"))).click()
                except:
                    pass
                title = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    (By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div/div[3]/div/h1"))).text
                #authors = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    #(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div/div[3]/div/h3[1]"))).text
                #institute = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
                    #(By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div/div[3]/div/h3[2]"))).text
                abstract = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "abstract-text"))).text
                '''
                try:
                    keywords = WebDriverWait(driver, 0.5+ran).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "keywords"))).text[:-1]
                    cssci = WebDriverWait(driver, 0.5+ran).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[3]/div/div/div[1]/div[1]/a[2]"))).text
                except:
                    keywords = '无'
                    cssci = 'NULL'
                '''
                url = driver.current_url
                # 获取下载链接
                # link = WebDriverWait( driver, 10 ).until( EC.presence_of_all_elements_located((By.CLASS_NAME  ,"btn-dlcaj") ) )[0].get_attribute('href')
                # link = urljoin(driver.current_url, link)

                # 写入文件
                
                res = f"{count}\t{date[:11]}\t{source}\t{title}\t{database}\t{abstract}\t{url}".replace(
                        "\n", "") + "\n"
                #print(f"{count}\t{date[:11]}\t{source:.35s}\t{title}")
                # 打印当前爬取的文献
                #print('%s\t%s\t%-26s%s\t%s' %(count, date[:11],source,title,database))
                with open(f'CNKI_{namer}.tsv', 'a', encoding='gbk') as f:
                    f.write(res)
                #count += 1
                error=0

            #error重名了
            except Exception as errorinf:
                print(f" 第{count} 条爬取失败\n")
                print(errorinf)
                error+=1
                if error>=5:
                    title_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "fz14")))
                    i-=error
                    count-=error

                # 跳过本条，接着下一个
                continue
            finally:
                # 如果有多个窗口，关闭第二个窗口， 切换回主页
                #print(title_list[0])
                #print(len(title_list))
                #print('\n')
                n2 = driver.window_handles
                if len(n2) > 1:
                    driver.close()
                    driver.switch_to.window(n2[0])
                
                # 使用共享内存列表监视所有进程的情况
                shared_list[num-1]=wxnum
                #print('已获取文献 {:>4d} 篇'.format(sum(shared_list)))
                print(shared_list)

                # 写入json方便其他文件获取状态
                json_file_name = 'num.json'
                # 使用 json.dump 将列表保存到 JSON 文件
                with open(json_file_name, 'w') as json_file:
                    json.dump(list(shared_list), json_file)
                
                # 计数,判断需求是否足够
                count += 1
                wxnum += 1
                


        if count > papers_need:
            #driver.close()
            break
        else:
            # 切换到下一页
            try:
                WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@id='PageNext']"))).click()
                duandian=0
            except:
                print('没有下一页')
                break
    # 用quit不用close
    driver.quit()

def fix_need_paper(papers_need,theme):
    try:
        res_unm = int(how_much_paper(open_page(webserver(), theme)))
    except Exception as aaa:
        print("openpage出错了：{}".format(aaa))
        res_unm=papers_need

    # 判断所需是否大于总篇数
    papers_need = papers_need if (papers_need <= res_unm) else res_unm
    return papers_need
def search(theme,papers_need,duandian = 0):
    global shared_list
    # 共享内存列表
    shared_list = mp.Manager().list()
    for i in range(11):
        shared_list.append(0)
    namer=theme.replace('\"','\'')
    namer=namer.replace('*','_')

    res = f"序号\t日期\t来源\t标题\t类型\t摘要\t链接\t".replace(
            "\n", "") + "\n"
    print(res)
    if os.path.exists(f'CNKI_{namer}.tsv'):
        with open(f'CNKI_{namer}.tsv', 'r', encoding='gbk') as f:
            #判断是不是空文件 空文件再写入这些
            size = len(f.readlines())
            print("已存在TSV 文献数: %d篇" % (size))
    else:
        with open(f'CNKI_{namer}.tsv', 'a', encoding='gbk') as f:
            f.write(res)

    papers_need=fix_need_paper(papers_need,theme)
    shared_list[-1]=papers_need
    
    json_file_name = 'num.json'
    # 使用 json.dump 将列表保存到 JSON 文件
    with open(json_file_name, 'w') as json_file:
        json.dump(list(shared_list), json_file)

    process_list = []

    p1 = Process(target=crawl, args=(shared_list,int(papers_need/4), theme,duandian,1))
    p1.start()
    p2 = Process(target=crawl, args=(shared_list,int(papers_need/4), theme,int(papers_need/4),2))
    p2.start()
    p3 = Process(target=crawl, args=(shared_list,int(papers_need/4), theme,int(papers_need/2),3))
    p3.start()
    #最后一个进程把小数后面的包了
    p4 = Process(target=crawl, args=(shared_list,papers_need-3*int(papers_need/4), theme,int(papers_need*3/4),4))
    p4.start()
    
    process_list.append(p1)
    process_list.append(p2)
    process_list.append(p3)
    process_list.append(p4)
    for t in process_list:
        t.join()
    json_file_name = 'num.json'
    # 使用 json.dump 将列表保存到 JSON 文件
    with open(json_file_name, 'w') as json_file:
        json.dump([0,0,0,0,0,0,0,0,0,0,0], json_file)
    for process in process_list:
        process.terminate()
    

if __name__ == "__main__":
    #pyinstaller打包时要这样处理多进程，不然会循环调用
    mp.freeze_support()
    # 输入需要搜索的内容
    theme = input('文献主题： ')
    papers_need = int(input('所需篇数:  '))

    #theme = "稻鱼"
    #papers_need = 400
    duandian = 0

    search(theme,papers_need,duandian)
    '''
    namer=theme.replace('\"','\'')
    namer=namer.replace('*','')
    res = f"序号\t日期\t来源\t标题\t类型\t摘要\t链接\t".replace(
            "\n", "") + "\n"
    print(res)
    with open(f'CNKI_{namer}.tsv', 'a', encoding='gbk') as f:
        f.write(res)

    process_list = []

    p1 = Process(target=crawl, args=(int(papers_need/4), theme,duandian))
    p1.start()
    p2 = Process(target=crawl, args=(int(papers_need/4), theme,int(papers_need/4)))
    p2.start()
    p3 = Process(target=crawl, args=(int(papers_need/4), theme,int(papers_need/2)))
    p3.start()
    p4 = Process(target=crawl, args=(int(papers_need/4), theme,int(papers_need*3/4)))
    p4.start()
    
    process_list.append(p1)
    process_list.append(p2)
    process_list.append(p3)
    process_list.append(p4)
    for t in process_list:
        t.join()
    '''



    


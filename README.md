# CNKI_VIEW
摘要：selenium/requests 知网爬虫以及附带图像界面的爬虫结果(表格)查看器 / a GUI viewer of crawl results of cnki with crawler based on selenium/requests and pyqt  

前言：爬虫得到的结果一般保存为csv这种表格文件，乍一看很美好😇  
但是一般的表格查看软件对这种表格没有专门适配，想看得舒服害得一个一个专门调整格式🤦‍♂️ 

# 特点
作为一款专为知网爬虫结果设计的表格查看器，可以：  
- 单独一个窗口显示摘要  
- 根据文献来源类型排序  
- 检测刊物是否在cscd库内  
- 直接在GUI中进行爬虫操作  
（多进程，实时显示进度）  
- 切换同级目录路径下的爬虫结果  
- 一个不断完善的设置界面，自定义阅读体验  

# 界面
<img width="1154" height="651" alt="image" src="https://github.com/user-attachments/assets/31fa4acb-7571-4300-8c2f-fa31ba4b4789" />

# 安装  
**PC下载后运行：**  
两个版本：lite版仅有查看功能，full版有爬虫功能  
selenium爬虫需要下载对应浏览器驱动msedgedriver  
request爬虫则不需要  
cscd中文库.csv下载后才有核心标注功能 
exe文件：[v1.0.0版本](https://github.com/Zagreus1892/CNKI_VIEW/releases/tag/First)  
> lite版本UI更新较快，源码已经更新组件随窗口自动缩放，1.0版本full版本暂未添加requests方式
> 

# 改进目标  
收藏功能  
内部排序  
设置表头显示信息  
优化读取pandas速度  
插件api


import pandas as pd

# 读取CSV文件
data = pd.read_csv("CNKI_浮游植物.csv", sep=',', encoding='gbk')

# 将数据写入TSV文件
data.to_csv("CNKI_浮游植物.tsv", index=False, sep='\t', encoding='gbk')
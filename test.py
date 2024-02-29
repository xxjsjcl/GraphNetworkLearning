import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import pandas as pd
import numpy as np
import seaborn as sns       # 封装了matplotlib的可视化包：https://seaborn.pydata.org/examples/index.html
import matplotlib as mpl
import matplotlib.pyplot as plt
## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

# 建立一张随机图
G = nx.gnp_random_graph(100, 0.02, seed=10374196)   # type:nx.Graph

fig = plt.figure("随机图", figsize=(8, 8))


# 分析随机图的节点的度
degree_list = G.degree()     # 得到节点的度，这是一个list
degree_sequence = sorted((d for n, d in G.degree()), reverse=True)  # 取出所有度并进行排序

sns.histplot(data=degree_sequence,binwidth=1)

plt.show()
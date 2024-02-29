# 配置环境
## 导入工具包
import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import matplotlib as mpl
print("数据可视化工具包_matplotlib:" + mpl.__version__)
import matplotlib.pyplot as plt
## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号


# 建立一张有向图
H = nx.DiGraph(nx.star_graph(7))
nx.draw(H,with_labels=True)

# 计算每个节点的PageRank
pageRank = nx.pagerank(H, alpha=0.8)   # alpha为算法的阻尼系数，默认为0.85
print(pageRank)

plt.show()
import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import matplotlib as mpl
print("数据可视化工具包_matplotlib:" + mpl.__version__)
import matplotlib.pyplot as plt
import numpy as np
print("数学函数和矩阵运算工具包_numpy:" + np.__version__)
## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

# 建立一张随机图
G = nx.gnp_random_graph(100, 0.02, seed=10374196)   # type:nx.Graph

fig = plt.figure("随机图", figsize=(8, 8))
nx.draw(G,node_size=50)

# 分析随机图的节点的度
degree_list = G.degree()     # 得到节点的度，这是一个list
degree_sequence = sorted((d for n, d in G.degree()), reverse=True)  # 取出所有度并进行排序
print(degree_sequence)
dmax = max(degree_sequence)

# 找到最大连通域子图
Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
## 上面那句的功能拆解开来大概是下面这段
# connect_componets_generator = nx.connected_components(G)  # 得到所有连通域，这是一个generator
# connect_componets = list(connect_componets_generator)     # 把他转换成list
# max_connect_component = sorted(connect_componets, key=len, reverse=True)[0]     # 把list按元素长度倒序排列，取第一个得到最大连通域
# Gcc = G.subgraph(max_connect_component)       # 在G中用最大连通域做一个子图

pos = nx.spring_layout(Gcc, seed=10396953)

fig = plt.figure("分析随机图节点的度", figsize=(8, 8))
axgrid = fig.add_gridspec(5, 4)
ax0 = fig.add_subplot(axgrid[0:3, :])

nx.draw_networkx_nodes(Gcc, pos, ax=ax0, node_size=20)
nx.draw_networkx_edges(Gcc, pos, ax=ax0, alpha=0.4)
ax0.set_title("随机图的最大联通子图")
ax0.set_axis_off()

ax1 = fig.add_subplot(axgrid[3:, :2])
ax1.plot(degree_sequence, "b-", marker="o")
ax1.set_title("度排名的散点图")
ax1.set_ylabel("Degree")
ax1.set_xlabel("Rank")

ax2 = fig.add_subplot(axgrid[3:, 2:])
degree_hist = np.unique(degree_sequence, return_counts=True)
ax2.bar(degree_hist[0],degree_hist[1])
ax2.set_title("度的直方图")
ax2.set_xlabel("Degree")
ax2.set_ylabel("# of Nodes")

fig.tight_layout()
plt.show()
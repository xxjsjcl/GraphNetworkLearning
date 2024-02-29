# 配置环境
## 导入工具包
import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import matplotlib as mpl
print("数据可视化工具包_matplotlib:" + mpl.__version__)
import matplotlib.pyplot as plt
import numpy as np
print("数学函数和矩阵运算工具包_numpy:" + np.__version__)
import operator as op
## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

# 用Barabási–Albert（BA）模型创建一个无标度网络
n = 1000
m = 2
seed = 20532
G = nx.barabasi_albert_graph(n, m, seed=seed)
print(G)

# 找到拥有最大的连接数的节点
node_and_degree = G.degree()
print(node_and_degree)
# operateor.itemgetter可以从某个对象获取特性下标的数据
# sorted返回排序后的列表
sorted_node_by_degree = sorted(node_and_degree, key=op.itemgetter(1))
print(sorted_node_by_degree)
(largest_hub, degree) = sorted_node_by_degree[-1]

# 用这个节点作为中心节点，生成一个Ego图
G_ego = nx.ego_graph(G, largest_hub)   # nx生成ego图的函数，需要传入图和中心节点
print(G_ego)

# 可视化图
fig = plt.figure('Ego图',figsize=(10,10), constrained_layout=True)
plt.title('Ego图')
pos = nx.spring_layout(G_ego, seed=seed)
nx.draw(G_ego, pos, node_color="b", node_size=50, with_labels=False)

# 把中心节点重点画出来
options = {"node_size": 300, "node_color": "r"}
nx.draw_networkx_nodes(G_ego, pos, nodelist=[largest_hub], **options)

plt.show()
import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import matplotlib as mpl
print("数据可视化工具包_matplotlib:" + mpl.__version__)
import matplotlib.pyplot as plt
import itertools

## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['Microsoft YaHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

# 建立一个图
G = nx.karate_club_graph()  # type:nx.Graph
pos = nx.spring_layout(G, seed=123)
plt.figure()
nx.draw(G,pos=pos)

# 指定Graphlet
target_Graphlet = nx.complete_graph(4)  # type:nx.Graph
plt.figure()
nx.draw(target_Graphlet,pos=pos)

# 在全图中匹配子图，统计个数
print('-------------------Graph中所有Graphlet------------------------')
plt.figure()
num = 0
for sub_nodes in itertools.combinations(G.nodes(),len(target_Graphlet.nodes())): # 返回所有G图中3个节点（子图的节点个数）的所有节点组合
    sub_G = G.subgraph(sub_nodes)   # 用取出来的节点生成一个子图
    # 判断子图是不是连通的，如果是连通的，再判断和Graphlet是不是同构的
    if nx.is_connected(sub_G) and nx.is_isomorphic(sub_G, target_Graphlet):
        num = num + 1
        print(sub_G.edges())

        nx.draw(sub_G,pos=pos)

print(f"Graphlet数量：{num}")




plt.show()
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

# 生成一个棒棒糖图
G = nx.lollipop_graph(4, 7)  # type:nx.Graph
pos = nx.spring_layout(G, seed=3068)  # Seed layout for reproducibility
nx.draw(G, pos=pos, with_labels=True)


# 图特征分析
## 图的离心率，每个节点都有一个离心率，它是离这个节点最远的距离
print(f"eccentricity: {nx.eccentricity(G)}")
## 图的半径，所有节点离心率的最小值
print(f"radius: {nx.radius(G)}")
## 图的直径，所有节点离心率的最大值，图中距离最远的2个点的距离
print(f"diameter: {nx.diameter(G)}")
## 中心节点：离心率与半径相等的点
print(f"center: {nx.center(G)}")
## 外围节点：离心率与直径相等的点
print(f"periphery: {nx.periphery(G)}")
## 图的密度，图的密度指的是图中连接的数量和这个图所有可能的连接数量的比例
## 对于无向图 density = edgeNum/(nodeNum*(nodeNum-1)/2) 
## 对于有向图，边的数量是无向图的2倍，所以 density = edgeNum/(nodeNum*(nodeNum-1)) 
print(f"density: {nx.density(G)}")

## 最短距离
print('3号节点到其他节点的最短距离:')
shortest_path_length = nx.shortest_path_length(G,3)
print(shortest_path_length)
shortest_path_length = nx.shortest_path_length(G,3,5)
print(f"3号节点到5号节点的最短距离：{shortest_path_length}")

## 最短路径
shortest_path = nx.shortest_path(G,3,5)
print(f"3号节点到5号节点的最短路径：{shortest_path}")


## 平均最短距离
### 计算每2个节点间的最短距离
pathlengths = []
print("每2个节点间的最短距离，格式：起始节点 {目标节点:最短距离, }")
for v in G.nodes():
    spl = dict(nx.single_source_shortest_path_length(G, v))
    print(f"{v} {spl} ")
    for p in spl:
        pathlengths.append(spl[p])
### 平均最短路径距离的定义是: 所有节点的最短路径距离和/所有可能的路径数
print(f"平均最短路径长度 {(sum(pathlengths)/2)/ (len(G)*(len(G)-1)/2)}")
print(f"平均最短路径长度 {nx.average_shortest_path_length(G)}")

# 路径长度的直方图，统计每个路径长度的个数
pathlength_hist = np.unique(pathlengths, return_counts=True)
print(pathlength_hist)

print("路径长度直方图：")
for i in range(len(pathlength_hist[0])):
    print(f"{pathlength_hist[0][i]} : {pathlength_hist[1][i]}")

plt.show()
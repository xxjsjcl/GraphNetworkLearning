# 配置环境
## 导入工具包
import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import torch
print("神经网络工具包_pythrch:" + torch.__version__)
import matplotlib as mpl
print("数据可视化工具包_matplotlib:" + mpl.__version__)
import matplotlib.pyplot as plt
import numpy as np
print("数学函数和矩阵运算工具包_numpy:" + np.__version__)
import pandas as pd
print("数据分析和导入工具包_pandas:" + pd.__version__)
## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

# nx.draw可视化图
fig = plt.figure("NetworkX图可视化", figsize=(16, 5), constrained_layout=True)
plt.suptitle("NetworkX图可视化")
axgrid = fig.add_gridspec(nrows=2,ncols=8)  # 给图分成2行8列的格子，后面的子图可以按需分配格子以分别确定子图像大小

G = nx.Graph(nx.grid_2d_graph(4,4,create_using=nx.Graph))

## 默认可视化
ax0 = fig.add_subplot(axgrid[:, 0:2])  # 把子图画到前3个格子里
ax0.set_title("默认可视化")
pos = nx.spring_layout(G,seed=123)
nx.draw(G, pos=pos)

## 不显示节点
ax0 = fig.add_subplot(axgrid[:, 2:4])
ax0.set_title("不显示节点")
nx.draw(G, pos=pos, node_size=0, with_labels=False)

## 设置颜色
ax0 = fig.add_subplot(axgrid[:, 4:6])
ax0.set_title("设置颜色")
nx.draw(
    G = G,                      # 图
    pos = pos,                  # 节点位置
    node_color = '#A0CBE2',     # 节点颜色
    edgecolors = 'red',         # 节点轮廓颜色
    edge_color = 'blue',        # 连接颜色
    node_size = 800,            # 节点大小
    with_labels = False,        # 是否显示节点label
    width = 3                  # 连接宽度
)

## 画有向图
H = G.to_directed()
ax0 = fig.add_subplot(axgrid[:, 6:8])
ax0.set_title("画有向图")
nx.draw(
    G = H,                      # 图
    pos = pos,                  # 节点位置
    node_color = 'xkcd:orange', # 节点颜色
    node_size = 400,            # 节点大小
    edgecolors = 'xkcd:gray',   # 节点轮廓颜色
    arrowsize = 10,             # 箭头大小
    width = 2                   # 连接宽度
)

## 设置每个节点的坐标
fig = plt.figure("设置每个节点的坐标", figsize=(12, 12), constrained_layout=True)
plt.suptitle("设置每个节点的坐标")
axgrid = fig.add_gridspec(nrows=4,ncols=4)  # 给图分成2行8列的格子，后面的子图可以按需分配格子以分别确定子图像大小

### 新建一张无向图
G = nx.Graph(nx.house_graph(create_using=nx.Graph))
pos = nx.spring_layout(G,seed=123)

ax0 = fig.add_subplot(axgrid[0:2, 0:2])  # 把子图画到前3个格子里
ax0.set_title("无向图，未设置节点坐标")
nx.draw(G, pos=pos, with_labels=True)

### 设置每个节点可视化时的坐标
pos = {0:(0,0),1:(-1,0.3),2:(2,0.17),3:(4,0.25),4:(5,0.03)} 
#### 可视化设置可以写进一个字典
options = {
    'with_labels':True,             # 是否显示label
    'font_size': 28,                # 字号
    'node_size': 800,               # 节点大小
    'node_color': 'xkcd:orange',    #
    'edgecolors': 'xkcd:gray',
    'linewidths': 3,                # 节点轮廓宽度
    'width':3,                      # 连接的线宽
}

ax0 = fig.add_subplot(axgrid[0:2, 2:4])  # 把子图画到前3个格子里
ax0.set_title("无向图，设置每个节点的坐标")
ax0.margins(0.2)
nx.draw(G, pos=pos, **options)
# nx.draw_networkx(G, pos=pos, **options)

### 新建一张有向图
H = nx.DiGraph([(0,3),(1,3),(2,4),(3,5),(3,6),(4,6),(5,6)])
pos = nx.spring_layout(H,seed=123)

ax0 = fig.add_subplot(axgrid[2:4, 0:2])
ax0.set_title("有向图，未设置节点坐标")
nx.draw(H, pos=pos, with_labels=True)

### 以栅格形式可视化
#### 可视化时每列包含的节点
left_nodes = [0, 1, 2]
middle_nodes = [3, 4]
right_nodes = [5, 6]

#### 计算可视化时每个节点的坐标
pos = {n:(0,i) for i,n in enumerate(left_nodes)}
pos.update({n:(1,i+0.5) for i,n in enumerate(middle_nodes)})
pos.update({n:(2,i+0.5) for i,n in enumerate(right_nodes)})
print(pos)

ax0 = fig.add_subplot(axgrid[2:4, 2:4])
ax0.set_title("有向图，设置每个节点的坐标")
nx.draw(H, pos=pos, **options)


## 分布绘制图，每次绘制特定的节点和边
fig = plt.figure("分布绘制图", figsize=(8, 8), constrained_layout=True)
plt.suptitle("每次绘制部分节点和边")
axgrid = fig.add_gridspec(nrows=4,ncols=4) 

G = nx.Graph(nx.house_graph(create_using=nx.Graph))
pos = {0:(0,0),1:(1,0),2:(0,1),3:(1,1),4:(0.5,2)} 
print(G.nodes)
print(G.edges)
### 绘制部分节点，不设置nodelist就是全画
nx.draw_networkx_nodes(G, pos=pos, node_size=1000, nodelist=[0,1,2,3],node_color='xkcd:lightblue')
nx.draw_networkx_nodes(G, pos=pos, node_size=1000, nodelist=[4],node_color='xkcd:orange')
### 绘制连接，不设置edgelist就是全画
nx.draw_networkx_edges(G, pos=pos, edgelist=[(0, 1), (0, 2), (1, 3), (2, 3)], alpha=1, width=6, edge_color='xkcd:black')
nx.draw_networkx_edges(G, pos=pos, edgelist=[(2, 4), (3, 4)], alpha=0.5, width=6, edge_color='xkcd:red')

plt.axis('off')
plt.show()


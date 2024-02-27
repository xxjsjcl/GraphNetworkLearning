# 配置环境
## 导入工具包
import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import numpy as np
print("数学函数和矩阵运算工具包_numpy:" + np.__version__)
import pandas as pd
print("数据分析和导入工具包_pandas:" + pd.__version__)
import matplotlib as mpl
print("数据可视化工具包_matplotlib:" + mpl.__version__)
import matplotlib.pyplot as plt
## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

# 使用连接表、邻接表、邻接矩阵创建图
## 导入连接表，注意清洗数据，为了展示这里简化了数据，数据源：[http://www.openkg.cn/dataset/ch4masterpieces]
df = pd.read_csv(r'Data\四大名著人物关系\三国演义\triples_simple.csv')
print(df,end='\n\n')

## 通过连接表创建一个有向图
print('----------创建图，通过连接表给图添加边----------')
### 创建一个空的有向图
G = nx.DiGraph()
print(G,end='\n\n')
### 提取dataframe中的'head'和'tail'列组合成元组，再组合成列表，这样就得到了所有的边
edges_total = [edge for edge in zip(df['head'], df['tail'])]  
print(edges_total,end='\n\n')
print(len(edges_total),end='\n\n')
### 从边的列表里添加边到图
G.add_edges_from(edges_total)

## 查看全图属性
print('----------查看图的属性----------')
print(G,end='\n\n') # 全图属性
print(G.nodes,end='\n\n') # 所有节点
print(G.nodes(data=True),end='\n\n') # 返回带属性的节点
print(len(G),end='\n\n') # 节点数
print(G.edges,end='\n\n') # 所有连接
print(len(G.edges),end='\n\n') # 连接数
print(G.size(),end='\n\n') # 连接数，或所有连接的权重和
print(G.edges('关羽'),end='\n\n')  # 提取与节点'关羽'相连的边

## 可视化图
fig = plt.figure("三国人物关系图", figsize=(15, 15), constrained_layout=True)
plt.suptitle("三国人物关系图")
pos = nx.spring_layout(G, seed=123)
nx.draw(G, with_labels=True)
plt.show()

## 保存连接表，读取连接表建立图
print('----------保存连接表----------')
edge_list = nx.generate_edgelist(G)  # 生成连接表
for line in edge_list:
    print(line)
### 用write_edgelist函数直接把连接表写入文件，如果分隔符用","的话，文件和csv文件没有本质区别，只是没有表头
nx.write_edgelist(G,path=r'Data\四大名著人物关系\三国演义\graph.edgelist',delimiter=',')
print('----------读取连接表建立图----------')
### 用read_edgelist函数读取连接表并生成图，默认生成的是无向图，其他类型图需要指定生成函数
G2 = nx.DiGraph(nx.read_edgelist(path=r'Data\四大名著人物关系\三国演义\graph.edgelist',delimiter=',', create_using=nx.DiGraph))
print(G2)

## 保存和载入邻接表（Adjacency List）
print('----------保存邻接表----------')
adj_list = nx.generate_adjlist(G)
for line in adj_list:
    print(line)
### 用write_adjlist函数将图保存成邻接表
nx.write_adjlist(G,path=r'Data\四大名著人物关系\三国演义\graph.adjlist',delimiter=',')
print('----------读取邻接表建立图----------')
### 读取邻接表生成图
G3 = nx.DiGraph(nx.read_adjlist(path=r'Data\四大名著人物关系\三国演义\graph.adjlist',delimiter=',', create_using=nx.DiGraph))
print(G3)

## 从邻接矩阵建立图
print('----------读取邻接矩阵建立图----------')
df = pd.read_csv(r'Data\分子结构\mol_bonds.csv', delimiter=',', header=None)
print(df)
G4 = nx.from_pandas_adjacency(df=df,create_using=nx.Graph)
print(G4)
fig = plt.figure("分子结构图", figsize=(15, 15), constrained_layout=True)
plt.suptitle("分子结构图")
pos = nx.spring_layout(G4, seed=123)
nx.draw(G4, with_labels=True)
plt.show()
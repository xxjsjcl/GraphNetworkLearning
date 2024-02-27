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

# 创建一个空图
print('----------创建一个无向图----------')
G = nx.Graph()
print(G.is_directed())
print('----------编辑整张图的属性----------')
G.graph['Name'] = 'HelloWorld'
print(G.graph)
print('----------创建一个有向图----------')
H = nx.DiGraph()
print(H.is_directed())

# 创建节点
print('----------创建节点----------')
G.add_node('刘备',武器='雌雄双股剑',武力=80,智力=85)
G.add_node('赵云',武器='青钢剑',武力=95,智力=80)
G.add_nodes_from([('关羽',{'武器':'青龙偃月刀','武力':90,'智力':90}),
                  ('张飞',{'武器':'丈八蛇矛','武力':85,'智力':80}),
                  ('吕布',{'武器':'方天画戟','武力':100,'智力':70})])
for node in G.nodes(data=True):
    print(node)

# 创建连接并设置连接属性
print('----------创建单个连接并设置连接属性----------')
G.add_edge('刘备','赵云',weight=0.8,like=5)
print(G.edges)  # 查看所有的边
print('----------创建多个连接并设置连接属性----------')
G.add_edges_from([('刘备','关羽', {'weight':1,'like':5}),
                  ('刘备','张飞', {'weight':1,'like':5}),
                  ('关羽','张飞', {'weight':1,'like':5}),
                  ('刘备','吕布', {'weight':0.5,'like':2}),])
print(G.edges)  # 查看所有的边

print('----------查看连接属性----------')
print(G.edges)  # 查看所有的边
print(G.edges['刘备','关羽'])  # 查看某条边的属性
print(G.edges(data='刘备'))    # 查看与某节点连接的所有边
print(G.edges(data=True))     # 查看所有边及属性
print(G.degree)               # 查看连接数（度）
print(G.degree['刘备'])       # 查看指定节点的连接数

# 查看某节点所有相邻节点
for neighbor in G.neighbors('刘备'):
    print(neighbor)

# 可视化
plt.figure()
nx.draw(G,with_labels=True)


plt.show()

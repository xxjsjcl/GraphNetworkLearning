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
G = nx.Graph()

# 添加单个节点
print('----------添加单个节点----------')
G.add_node('刘备')
print(G.nodes)
G.add_node(2)  # 节点可以是任意可哈希对象
print(G.nodes)

# 添加多个节点
print('----------添加多个节点----------')
G.add_nodes_from(['诸葛亮','曹操'])
print(G.nodes)
G.add_nodes_from(range(101,105))
print(G.nodes)

# 添加带属性的节点
print('----------添加带属性的节点----------')
G.add_nodes_from([('关羽',{'武器':'青龙偃月刀','武力':90,'智力':90}),
                  ('张飞',{'武器':'丈八蛇矛','武力':85,'智力':80}),
                  ('吕布',{'武器':'方天画戟','武力':100,'智力':70})])
print(G.nodes)

nx.draw(G, with_labels=True, node_color='pink')
plt.show()
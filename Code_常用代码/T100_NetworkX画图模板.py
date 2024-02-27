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
## 开启交互模式，show()画图不会阻塞程序运行，但会马上消失
plt.ion()

# 经典图结构
fig = plt.figure("Network绘图演示", figsize=(16, 8), constrained_layout=True)
plt.suptitle("Network绘图演示")  # 总title
axgrid = fig.add_gridspec(nrows=2,ncols=8)  # 给图分成2行8列的格子，后面的子图可以按需分配格子以分别确定子图像大小

## with_labels=指定是否显示节点的名字
G = nx.complete_graph(7)
ax0 = fig.add_subplot(axgrid[0, 0:2])  # 把子图画到前3个格子里
ax0.set_title("全连接无向图")
nx.draw(G, with_labels=True, edge_color='b', node_color='g', node_size=1000)
## 全连接有向图
G = nx.complete_graph(7, nx.DiGraph())
ax1 = fig.add_subplot(axgrid[0, 2:4])
ax1.set_title("全连接有向图")
nx.draw(G)

## 环状图
G = nx.cycle_graph(7)
ax2 = fig.add_subplot(axgrid[0, 4:6])
ax2.set_title("环状图")
nx.draw(G)

## 梯状图
G = nx.ladder_graph(7)
ax3 = fig.add_subplot(axgrid[0, 6:8])
ax3.set_title("梯状图")
nx.draw(G)

## 线性图
G = nx.path_graph(7)
ax4 = fig.add_subplot(axgrid[1, 0:2])
ax4.set_title("线性图")
nx.draw(G)

## 星状图
G = nx.star_graph(7)
ax5 = fig.add_subplot(axgrid[1, 2:4])
ax5.set_title("星状图")
nx.draw(G)

## 轮辐图
G = nx.wheel_graph(7)
ax6 = fig.add_subplot(axgrid[1, 4:6])
ax6.set_title("轮辐图")
nx.draw(G)

## 二项树
G = nx.binomial_tree(5)
ax6 = fig.add_subplot(axgrid[1, 6:8])
ax6.set_title("二项树")
nx.draw(G)

# 可以在程序最后关闭交互模式，一起再显示出来
plt.ioff()
plt.show()
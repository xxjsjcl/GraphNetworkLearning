# 配置环境
## 导入工具包
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

# 创建一个有向图
seed = 13648
MH = nx.random_k_out_graph(10, 3, 0.5, seed=seed)
pos = nx.spring_layout(MH, seed=seed)

# 可视化图
fig = plt.figure("有向图可视化", figsize=(16, 8), constrained_layout=True)
plt.suptitle("有向图可视化")
axgrid = fig.add_gridspec(nrows=2,ncols=8)  # 给图分成2行8列的格子，后面的子图可以按需分配格子以分别确定子图像大小

ax0 = fig.add_subplot(axgrid[:, 0:4])  # 把子图画到前3个格子里
ax0.set_title("默认可视化")

nx.draw(MH, pos=pos, with_labels=True)

# 修饰图
ax0 = fig.add_subplot(axgrid[:, 4:8])  # 把子图画到前3个格子里
ax0.set_title("修饰图")

node_sizes = [3 + 100 * i for i in range(len(MH))]
M = MH.number_of_edges()
edge_colors = range(2, M + 2)
edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
cmap = plt.cm.plasma

nodes = nx.draw_networkx_nodes(MH, pos, node_size=node_sizes, node_color="indigo")
edges = nx.draw_networkx_edges(
    MH,
    pos,
    node_size=node_sizes,
    arrowstyle="->",
    arrowsize=10,
    edge_color=edge_colors,
    edge_cmap=cmap,
    width=4,
)

# 单独设置每条边的透明度
for i in range(M):
    edges[i].set_alpha(edge_alphas[i])

# 设置colorBar
pc = mpl.collections.PatchCollection(edges, cmap=cmap)
pc.set_array(edge_colors)
ax0.set_axis_off()
plt.colorbar(pc, ax=ax0)

plt.show()
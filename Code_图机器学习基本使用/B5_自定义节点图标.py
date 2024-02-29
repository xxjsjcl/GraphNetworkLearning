# 配置环境
## 导入工具包
import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import matplotlib as mpl
print("数据可视化工具包_matplotlib:" + mpl.__version__)
import matplotlib.pyplot as plt
import PIL   # 用于处理图片
## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

# 首先定义每个节点的自定义图片位置
icons = {
    "router": "Data\案例\Icons\icon-28.png",
    "switch": "Data\案例\Icons\icon-30.png",
    "PC": "Data\案例\Icons\icon-39.png",
}

# 读取图片
images = {k: PIL.Image.open(fname) for k, fname in icons.items()}

# 生成一个计算机网络的图
G = nx.Graph()

G.add_node("router", image=images["router"])
for i in range(1, 4):
    G.add_node(f"switch_{i}", image=images["switch"])
    for j in range(1, 4):
        G.add_node("PC_" + str(i) + "_" + str(j), image=images["PC"])

G.add_edge("router", "switch_1")
G.add_edge("router", "switch_2")
G.add_edge("router", "switch_3")
for u in range(1, 4):
    for v in range(1, 4):
        G.add_edge("switch_" + str(u), "PC_" + str(u) + "_" + str(v))

# 生成节点布局
pos = nx.spring_layout(G, seed=1734289230)

fig, ax = plt.subplots()

# 先画边，再单独把节点对应的图片画上

# 注意：min_source/target_margin参数作用于FancyArrowPatch objects.
# 必须使用'arrows=True'，强制将边的类型变为FancyArrowPatch
# 不想画箭头的话，使用'arrowstyle="-"'
nx.draw_networkx_edges(
    G,
    pos=pos,
    ax=ax,
    arrows=True,
    arrowstyle="-",
    min_source_margin=15,
    min_target_margin=15,
)

# Transform from data coordinates (scaled between xlim and ylim) to display coordinates
tr_figure = ax.transData.transform
# Transform from display to figure coordinates
tr_axes = fig.transFigure.inverted().transform

# 计算图片大小，相对于坐标轴
icon_size = (ax.get_xlim()[1] - ax.get_xlim()[0]) * 0.025
icon_center = icon_size / 2.0

# 在每个节点的位置画对应的图片
for n in G.nodes:
    xf, yf = tr_figure(pos[n])
    xa, ya = tr_axes((xf, yf))
    # get overlapped axes and plot icon
    a = plt.axes([xa - icon_center, ya - icon_center, icon_size, icon_size])
    a.imshow(G.nodes[n]["image"])
    a.axis("off")
plt.show()

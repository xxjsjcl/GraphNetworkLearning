# Graph Network Learning

 图机器学习记录。

## 图机器学习代码基本使用方法

### 1. 环境配置

#### （1）python环境

python：[https://www.python.org/](https://www.python.org/)

也可以使用anaconda管理python环境：[https://www.anaconda.com/](https://www.anaconda.com/)

#### （2）主要工具包

* networkX ：网络工具包，用于创建分析各种图和网络。[https://networkx.org/](https://networkx.org/)
* pytorch ：神经网络工具包。[https://pytorch.org/](https://pytorch.org/)
* matplotlib ：科学绘图工具包，用于数据可视化。[https://matplotlib.org/](https://matplotlib.org/)
* numpy ：数学函数库，主要用于矩阵运算。[https://numpy.org/](https://numpy.org/)
* pandas ：数据分析和处理库，主要用于导入和处理数据。[https://pandas.pydata.org/](https://pandas.pydata.org/)
* tqdm ：python自带进度条工具包。

#### （3）测试环境

```python
# 代码：Code_图机器学习基本使用\A1_配置环境.py
```

### 2. NetworkX基本使用方法

NetworkX基本使用方法。

参考文献：

* 基本教程：[https://networkx.org/documentation/stable/tutorial.html#](https://networkx.org/documentation/stable/tutorial.html#)
* 例子：[https://networkx.org/documentation/stable/auto_examples/index.html](https://networkx.org/documentation/stable/auto_examples/index.html)

#### （1）创建图，NetworkX内置图

使用NetworkX创建图。

NetworkX内置了一些预制好的图结构和图数据。

参考文献：

* 图的类型：[https://networkx.org/documentation/latest/reference/classes/index.html](https://networkx.org/documentation/latest/reference/classes/index.html)
* NetworkX内置的图：[https://networkx.org/documentation/latest/reference/generators.html](https://networkx.org/documentation/latest/reference/generators.html)
* 一些例子：[https://networkx.org/documentation/latest/auto_examples/graph/index.html](https://networkx.org/documentation/latest/auto_examples/graph/index.html)

```python
# 代码：Code_图机器学习基本使用\A2_创建图NetworkX内置图.py
```

#### （2）创建图，使用连接表和邻接表创建图

使用NetworkX，通过连接表和邻接表创建图，保存一个图的邻接表，通过邻接矩阵创建图。

参考文献：

* 格式转换：[https://networkx.org/documentation/latest/reference/convert.html](https://networkx.org/documentation/latest/reference/convert.html)
* 读写图：[https://networkx.org/documentation/latest/reference/readwrite/index.html](https://networkx.org/documentation/latest/reference/readwrite/index.html)

数据来源：

* 中国四大名著人物关系知识图谱：[http://www.openkg.cn/dataset/ch4masterpieces](http://www.openkg.cn/dataset/ch4masterpieces)

连接表：可以理解成记录了每一条边的表格，表格一般3列，第一列是头节点，第二列是尾节点，第三列是连接的名字或属性。

邻接表：可以理解成记录每个节点与其他节点关系的表格，表格第一列是每个节点，每个节点后面的列分别记录与其有连接的其他节点，有向图的话第一列都作为头节点。

邻接矩阵：以n*n的矩阵记录邻接关系，n为节点数，如果第m个节点和第n个节点有连接关系，则临界矩阵的第m行n列的数值不为0。

```python
# 代码：Code_图机器学习基本使用\A3_创建图_连接表和邻接表创建图.py
```

#### （3）创建节点

使用NetworkX创建单个节点、多个节点，添加并访问节点的属性。

在 NetworkX 中，节点可以是任何可哈希([hashable](https://link.zhihu.com/?target=https%3A//docs.python.org/3/glossary.html%23term-hashable))对象，例如，文本字符串、图像、XML对象、另一个图、自定义节点对象等。

在 NetworkX 中，节点的属性是一个python字典，因此可以使用字典操作的方法对节点属性进行操作。

参考文献：

* 创建图基础：[https://networkx.org/documentation/stable/tutorial.html](https://networkx.org/documentation/stable/tutorial.html)
* 更改图、节点、边的属性：[https://networkx.org/documentation/stable/tutorial.html#attributes](https://networkx.org/documentation/stable/tutorial.html#attributes)

```python
# 代码：Code_图机器学习基本使用\A4_创建节点.py
```

#### （4）创建连接

使用NetworkX创建连接，添加并访问连接的属性，本文中"连接"和"边"会混用，代表一个意思。

NetworkX可以创建无向图（Graph），有向图（Directed Graph），带权重的图（Weighted Graph）和多路图（MultiGraph）。

参考文献：

* 图的类型：[https://networkx.org/documentation/latest/reference/classes/index.html](https://networkx.org/documentation/latest/reference/classes/index.html)

NetworkX创建连接的方式和节点相似，可以参考节点的相关部分。

```python
# 代码：Code_图机器学习基本使用\A5_创建连接.py
```

### 3. NetworkX图的可视化方法

使用NetworkX和matplotlib可视化图。

#### （1）NetworkX的可视化函数

参考文献：

* draw函数中的参数：[https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw.html](https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw.html)
* 更多的设置参数：[https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx.html#](https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx.html#)
* 一些例子：[https://networkx.org/documentation/stable/auto_examples/drawing/index.html](https://networkx.org/documentation/stable/auto_examples/drawing/index.html)
* 常用的颜色：[xkcd.com/color/rgb/](https://xkcd.com/color/rgb/)

xkcd调色盘：见上链接，可以在matplotlib中直接使用的900多种常用色，使用方法如下

```python
color='xkcd:red'
```

![xkcd](https://github.com/xxjsjcl/GraphNetworkLearning/blob/main/image/README/1709017623781.png)

```python
# 代码：Code_图机器学习基本使用\B1_NetworX图可视化.py
#       Code_常用代码\T100_NetworkX画图模板.py
```

#### （2）图可视化例子，美国128城市交通关系无向图

参考文献：

* 数据源文件：[https://networkx.org/documentation/stable/auto_examples/drawing/plot_knuth_miles.html](https://networkx.org/documentation/stable/auto_examples/drawing/plot_knuth_miles.html)

```python
# 代码：Code_图机器学习基本使用\B2_例子_美国128城市交通连接图.py
```

#### （3）有向图可视化

参考文献：

* 可视化例子：[https://networkx.org/documentation/latest/auto_examples/drawing/plot_directed.html#sphx-glr-auto-examples-drawing-plot-directed-py](https://networkx.org/documentation/latest/auto_examples/drawing/plot_directed.html#sphx-glr-auto-examples-drawing-plot-directed-py)

```python
# 代码：Code_图机器学习基本使用\B3_有向图可视化.py
```

#### （4）多路图(MultiDiGraph)可视化例子，国际象棋对局

对多路图可视化的例子，数据1886-1985年国际象棋冠军赛对局，节点大小表示胜利次数，边的宽度表示对局次数

参考文献：

* 可视化例子：[https://networkx.org/documentation/latest/auto_examples/drawing/plot_chess_masters.html#sphx-glr-auto-examples-drawing-plot-chess-masters-py](https://networkx.org/documentation/latest/auto_examples/drawing/plot_chess_masters.html#sphx-glr-auto-examples-drawing-plot-chess-masters-py)
* 数据源：[https://chessproblem.my-free-games.com/PGN/WCC.zip](https://chessproblem.my-free-games.com/PGN/WCC.zip)

```python
# 代码：Code_图机器学习基本使用\B4_例子_国际象棋对局.py

# 注意：这个代码有一个坑，在使用matplotlib新建figure的时候，不能先于networkx的kamada_kawai_layout执行，否则会报错，原因不明。
# 这样执行会报错
fig,ax = plt.subplots(figsize=(12, 12))
pos = nx.kamada_kawai_layout(G)
# 这样执行可以正常运行
pos = nx.kamada_kawai_layout(G)
fig,ax = plt.subplots(figsize=(12, 12))
```

#### （5）自定义节点图标

自定义network中节点的图标，处理图片使用了PIIL(pillow)库。

参考文献

* 自定义节点例子：[https://networkx.org/documentation/stable/auto_examples/drawing/plot_custom_node_icons.html#sphx-glr-auto-examples-drawing-plot-custom-node-icons-py](https://networkx.org/documentation/stable/auto_examples/drawing/plot_custom_node_icons.html#sphx-glr-auto-examples-drawing-plot-custom-node-icons-py)
* PIL库的使用方法：[https://pillow.readthedocs.io/en/stable/](https://pillow.readthedocs.io/en/stable/)

```python
# 代码：Code_图机器学习基本使用\B5_自定义节点图标.py
```

#### （6）自我中心图（Ego图）

在NetworkX中创建Ego图，并找出连接数最大的主节点，构建以主节点为中心的邻域子图。

Ego图：存在一个中心节点，和所有的其他节点都有连接。

参考文献：

* Ego图例子：[https://networkx.org/documentation/stable/auto_examples/drawing/plot_ego_graph.html#sphx-glr-auto-examples-drawing-plot-ego-graph-py](https://networkx.org/documentation/stable/auto_examples/drawing/plot_ego_graph.html#sphx-glr-auto-examples-drawing-plot-ego-graph-py)

```python
# 代码：Code_图机器学习基本使用\B6_自我中心图.py
G_ego = nx.ego_graph(G, largest_hub)
```

### 4. NetworkX计算图的特征

使用NetworkX计算图的特征

参考文献：

* NetworkX算法：[https://networkx.org/documentation/stable/reference/algorithms/index.html](https://networkx.org/documentation/stable/reference/algorithms/index.html)

#### （1）PageRank节点重要度

计算有向图节点的PageRank节点重要度。

PageRank算法最初是用来评估网页重要性的，其核心思路就是在有向图上根据其边的分布和权重进行随机游走，每个时刻都可以计算出走到每个节点的概率，随着时间的延长，走到每个节点的概率趋于平稳，平稳状态下（时间区域无穷大）走到每个节点的概率即为节点的PageRank。

参考文献：

* PageRank算法：[https://networkx.org/documentation/stable/reference/algorithms/link_analysis.html](https://networkx.org/documentation/stable/reference/algorithms/link_analysis.html)
* PageRank定义：[PageRank算法详解 - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/137561088#%E6%9C%89%E5%90%91%E5%9B%BE%E5%92%8C%E9%9A%8F%E6%9C%BA%E6%B8%B8%E8%B5%B0%E6%A8%A1%E5%9E%8B)

```python
# 代码：Code_图机器学习基本使用\C1_PageRank节点重要度.py
pageRank=nx.pagerank(H)
```

#### （2）节点连接数分析

节点连接数即是节点的度，本文中会混用，节点的度是与该节点连接的所有边的数量。有向图中，根据边的方向，还可以统计从节点出发的边的数量（出度）和进入节点的边的数量（入度）。

参考文献：

* 节点度分析：[https://networkx.org/documentation/stable/auto_examples/drawing/plot_degree.html#sphx-glr-auto-examples-drawing-plot-degree-py](https://networkx.org/documentation/stable/auto_examples/drawing/plot_degree.html#sphx-glr-auto-examples-drawing-plot-degree-py)

```python
# 代码：Code_图机器学习基本使用\C2_节点度分析.py
degree = G.degree()		# G可以是有向图或无向图
out_degree = H.out_degree()	# H是一个有向图
in_degree = H.in_degree()
```

#### （3）图特征分析

用NetworkX分析图的基本特征。

这个例子里面分析了图的半径、直径、离心率、中心节点和外围节点等基本特征，还计算了节点间的最短路径和图的平均最短路径长度。

每个特征的具体涵义可以参考图论相关内容。

参考文献：

* 图特征例子：[https://networkx.org/documentation/stable/auto_examples/basic/plot_properties.html#sphx-glr-auto-examples-basic-plot-properties-py](https://networkx.org/documentation/stable/auto_examples/basic/plot_properties.html#sphx-glr-auto-examples-basic-plot-properties-py)
* 图的基本属性：[https://zhuanlan.zhihu.com/p/261156808](https://zhuanlan.zhihu.com/p/261156808)

```python
# 代码：Code_图机器学习基本使用\C3_图特征分析.py
# 注意：官方例子中计算平均最短路径距离的代码有误，结果不对，直接调用networkx计算平均最短路径的函数结果是正确的
nx.average_shortest_path_length(G)  # 函数计算出的结果是正确的
print(f"average shortest path length {sum(pathlengths) / len(pathlengths)}")	# 这句计算过程是不符合平均最短路径距离的定义的
```

#### （4）节点特征分析

用NetworkX计算有向图和无向图的节点特征。

例子中计算了无向图和有向图的节点的度，度中心性Degree Centrality，特征向量中心性Eigenvector Centrality，中介中心性Between Centrality，紧密中心性Closeness Centrality等。

还演示了PageRank，Katz中心性，HITS算法，聚集系数，

参考文献：

* 图的一些基本概念：[https://zhuanlan.zhihu.com/p/380945503](https://zhuanlan.zhihu.com/p/380945503)
* 节点特征的概念：[https://zhuanlan.zhihu.com/p/403076024](https://zhuanlan.zhihu.com/p/403076024) , [https://blog.csdn.net/lucienn/article/details/115418203](https://blog.csdn.net/lucienn/article/details/115418203) , [https://www.bilibili.com/video/BV1HK411175s/?spm_id_from=333.999.0.0&amp;vd_source=23da92f974a42dedec9c261159a41030](https://www.bilibili.com/video/BV1HK411175s/?spm_id_from=333.999.0.0&vd_source=23da92f974a42dedec9c261159a41030)
* HITS算法：[https://zhuanlan.zhihu.com/p/206965478](https://zhuanlan.zhihu.com/p/206965478)

end

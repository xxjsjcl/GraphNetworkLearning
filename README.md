# Graph Network Learning

 图机器学习记录。

## 图机器学习代码基本使用方法

### 1. 环境配置

（1）python环境

（2）主要工具包：

* networkX ：网络工具包，用于创建分析各种图和网络。[https://networkx.org/](https://networkx.org/)
* pytorch ：神经网络工具包。[https://pytorch.org/](https://pytorch.org/)
* matplotlib ：科学绘图工具包，用于数据可视化。[https://matplotlib.org/](https://matplotlib.org/)
* numpy ：数学函数库，主要用于矩阵运算。[https://numpy.org/](https://numpy.org/)
* pandas ：数据分析和处理库，主要用于导入和处理数据。[https://pandas.pydata.org/](https://pandas.pydata.org/)
* tqdm ：python自带进度条工具包。

（3）测试环境

```
代码：Code_图机器学习基本使用\A1_配置环境.py
```

### 2. NetworkX基本使用方法

NetworkX基本使用方法

参考文献：[https://networkx.org/documentation/stable/auto_examples/index.html](https://networkx.org/documentation/stable/auto_examples/index.html)

#### （1）创建图，NetworkX内置图

NetworkX内置了一些预制好的图结构和图数据

参考文献：

* [https://networkx.org/documentation/latest/reference/generators.html](https://networkx.org/documentation/latest/reference/generators.html)
* [https://networkx.org/documentation/latest/auto_examples/graph/index.html](https://networkx.org/documentation/latest/auto_examples/graph/index.html)

```
代码：Code_图机器学习基本使用\A2_创建图NetworkX内置图.py
```

#### （2）创建图，使用连接表和邻接表创建图

使用NetworkX，通过连接表和邻接表创建图，保存一个图的邻接表，通过邻接矩阵创建图

参考文献：

* 格式转换：[https://networkx.org/documentation/latest/reference/convert.html](https://networkx.org/documentation/latest/reference/convert.html)
* 读写图：[https://networkx.org/documentation/latest/reference/readwrite/index.html](https://networkx.org/documentation/latest/reference/readwrite/index.html)

数据来源：

* 中国四大名著人物关系知识图谱：[http://www.openkg.cn/dataset/ch4masterpieces](http://www.openkg.cn/dataset/ch4masterpieces)

连接表：可以理解成记录了每一条边的表格，表格一般3列，第一列是头节点，第二列是尾节点，第三列是连接的名字或属性

邻接表：可以理解成记录每个节点与其他节点关系的表格，表格第一列是每个节点，每个节点后面的列分别记录与其有连接的其他节点，有向图的话第一列都作为头节点

邻接矩阵：以n*n的矩阵记录邻接关系，n为节点数，如果第m个节点和第n个节点有连接关系，则临界矩阵的第m行n列的数值不为0

```
代码：Code_图机器学习基本使用\A3_创建图_连接表和邻接表创建图.py
```

#### （3）创建节点

使用NetworkX创建单个节点、多个节点

在 NetworkX 中，节点可以是任何可哈希([hashable](https://link.zhihu.com/?target=https%3A//docs.python.org/3/glossary.html%23term-hashable))对象，例如，文本字符串、图像、XML对象、另一个图、自定义节点对象等。

参考文献：

* 创建图基础：[https://networkx.org/documentation/stable/tutorial.html](https://networkx.org/documentation/stable/tutorial.html)
* 更改图、节点、边的属性：[https://networkx.org/documentation/stable/tutorial.html#attributes](https://networkx.org/documentation/stable/tutorial.html#attributes)

```
代码：Code_图机器学习基本使用\A4_创建节点.py
```

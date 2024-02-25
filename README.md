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

代码：Code_图机器学习基本使用\A1_配置环境.py

### 2. NetworkX基本使用方法

NetworkX基本使用方法

参考文献：[https://networkx.org/documentation/stable/auto_examples/index.html](https://networkx.org/documentation/stable/auto_examples/index.html)

#### （1）创建图，NetworkX内置图

NetworkX内置了一些预制好的图结构和图数据

参考文献：

* [https://networkx.org/documentation/latest/reference/generators.html](https://networkx.org/documentation/latest/reference/generators.html)
* [https://networkx.org/documentation/latest/auto_examples/graph/index.html](https://networkx.org/documentation/latest/auto_examples/graph/index.html)

代码：Code_图机器学习基本使用\A2_创建图NetworkX内置图.py

#### （2）创建图，使用连接表和邻接表创建图

使用NetworkX，通过连接表和邻接表创建图，通过邻接矩阵创建图

参考文献：

* [https://networkx.org/documentation/latest/reference/convert.html](https://networkx.org/documentation/latest/reference/convert.html)

代码：Code_图机器学习基本使用\A3_创建图_连接表和邻接表创建图.py

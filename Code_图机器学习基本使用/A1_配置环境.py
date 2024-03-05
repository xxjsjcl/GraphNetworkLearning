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
plt.rcParams['font.sans-serif']=['Microsoft YaHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

plt.plot([1,2,3],[100,500,300])
plt.title('中文测试',fontsize=25)
plt.xlabel('x轴',fontsize=15)
plt.ylabel('y轴',fontsize=15)
plt.show()

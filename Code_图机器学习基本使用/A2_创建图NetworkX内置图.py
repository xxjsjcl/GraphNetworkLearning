# 配置环境
import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import matplotlib
print("数据可视化工具包_matplotlib:" + matplotlib.__version__)
import matplotlib.pyplot as plt
# 配置windows 显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号


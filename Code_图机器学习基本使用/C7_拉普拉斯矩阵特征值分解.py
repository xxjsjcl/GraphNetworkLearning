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
plt.rcParams['font.sans-serif']=['Microsoft YaHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号


# 创建一个随机图
n = 100  # 1000 nodes
m = 500  # 5000 edges
G = nx.gnm_random_graph(n, m, seed=5040)    # type:nx.Grpah
pos = nx.spring_layout(G,seed=123)
fig = plt.figure()
nx.draw(G,pos=pos)

# 计算邻接矩阵
print('-----------------计算邻接矩阵---------------------')
A = nx.adjacency_matrix(G)
print(A.todense())

# 计算拉普拉斯矩阵
## 拉普拉斯矩阵计算公式： L = D - A
## 其中L为拉普拉斯矩阵；D为节点的度矩阵，只在对角线上有值；A为邻接矩阵
print('-----------------计算拉普拉斯矩阵---------------------')
L = nx.laplacian_matrix(G)
print(L.todense())

print('-----------------计算节点的度矩阵---------------------')
D = L + A
print(D.todense())

print('-----------------计算归一化拉普拉斯矩阵---------------------')
## 归一化公式： L_normalized = D^(-1/2)*L*D^(-1/2)
L_normalized = nx.normalized_laplacian_matrix(G)
L_n_matrix = L_normalized.todense()   # type:np.matrix
print(L_n_matrix)

## 归一化拉普拉斯矩阵绘图
fig = plt.figure("归一化拉普拉斯矩阵")
plt.title("归一化拉普拉斯矩阵")
plt.imshow(L_n_matrix)
plt.colorbar()


## 对拉普拉斯矩阵做特征值分解
print('-----------------对归一化拉普拉斯矩阵做特征值分解---------------------')
e = np.linalg.eigvals(L_n_matrix)
print(f"特征值为：\n{e}")
print(f"最大特征值为：{max(e)}")
print(f"最小特征值为：{min(e)}")

## 特征值分布可视化
fig = plt.figure("特征值分布直方图")
plt.title("特征值分布直方图")
plt.hist(e,bins=10)
plt.tick_params(labelsize=12)   # 设置坐标文字大小
plt.xlabel("特征值",fontsize=14)
plt.ylabel("频率",fontsize=14)





plt.show()
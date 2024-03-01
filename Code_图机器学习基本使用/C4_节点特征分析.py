import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import matplotlib as mpl
print("数据可视化工具包_matplotlib:" + mpl.__version__)
import matplotlib.pyplot as plt
import numpy as np
print("数学函数和矩阵运算工具包_numpy:" + np.__version__)
import operator as op
## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['Microsoft YaHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

# 统一格式的可视化方案
def My_Draw(G, pos, measures:dict, measure_name:str):
    """
    measures: 字典，value值为希望映射到节点颜色的值，key值为需要画的节点
    measure_name:图的名字
    """
    fig = plt.figure(measure_name)
    nodes = nx.draw_networkx_nodes(G, pos=pos, node_size=250, cmap=plt.cm.plasma,
                                   node_color=list(measures.values()),nodelist=measures.keys())
    nodes.set_norm(mpl.colors.SymLogNorm(linthresh=0.01,linscale=1,base=10))
    edges = nx.draw_networkx_edges(G, pos=pos)
    labels = nx.draw_networkx_labels(G, pos=pos)
    # nx.draw_networkx_labels(G, pos=pos)
    plt.title(measure_name)
    plt.axis('off')
    fig.colorbar(nodes)

## 节点的邻居
def Node_Neighbor(G,DiG):
    print('----------无向图节点的邻居----------')
    for node in G.nodes():
        print(f"{node}：{list(G.neighbors(node))}") 

    print('----------有向图节点的邻居,这里返回的是外邻居，即可以到达的节点----------')
    for node in DiG.nodes():
        print(f"{node}：{list(DiG.neighbors(node))}")

## 节点的度
def Node_Degree(G,DiG):
    print('----------无向图节点的度----------')
    print(f"列表形式：{list(nx.degree(G))}")
    print(f"字典形式：{dict(nx.degree(G))}")
    print("按度的大小进行排序：")
    print(f"列表排序：{sorted(list(G.degree()), key=op.itemgetter(1), reverse=True)}")
    print(f"字典排序：{sorted(dict(G.degree()).items(), key=op.itemgetter(1), reverse=True)}")

    My_Draw(G, pos=pos, measures=dict(G.degree()), measure_name="Nodes degree")

## 度中心性（Degree Centrality）
def Node_Degree_Centrality(G,DiG):
    ## 度中心性衡量节点在图中的重要性，核心思想就是节点的连接数越多重要性越大
    ## 计算方法为：nodeDegree/(nodesNum-1)，即节点的连接数/节点的最大可能连接数
    print(f"无向图的度中心性：\n{nx.degree_centrality(G)}")
    My_Draw(G, pos=pos, measures=dict(nx.degree_centrality(G)), measure_name="Nodes degree centrality") 

    print(f"有向图的度中心性：\n{nx.degree_centrality(DiG)}")
    print(f"有向图的入度中心性：\n{nx.in_degree_centrality(DiG)}")
    print(f"有向图的出度中心性：\n{nx.out_degree_centrality(DiG)}")
    My_Draw(DiG, pos=pos, measures=dict(nx.in_degree_centrality(DiG)), measure_name="Nodes in_degree centrality")
    My_Draw(DiG, pos=pos, measures=dict(nx.out_degree_centrality(DiG)), measure_name="Nodes out_degree centrality")

## 特征向量中心性（Eigenvector Centrality）
def Node_Eigenvector_Centrality(G,DiG):
    ## 核心思想是一个节点的重要度（中心性），不仅取决于节点本身是否重要（有足够多的邻居），也取决于邻居是否重要
    ## 一个节点的重要度=这个节点邻居节点重要度的和。
    ## 这是一个迭代的过程，最终会转化为求解特征方程的问题。
    # print(f"无向图的特征向量中心性：{nx.eigenvector_centrality(G)}")        # 2种函数结果不太一样,上面这种不能算有向图的
    print(f"无向图的特征向量中心性：\n{nx.eigenvector_centrality_numpy(G)}")    # 2种函数结果不太一样
    My_Draw(G, pos=pos, measures=dict(nx.eigenvector_centrality(G)), measure_name="Graph Nodes eigenvector centrality") 

    print(f"有向图的特征向量中心性：\n{nx.eigenvector_centrality_numpy(DiG)}")
    My_Draw(DiG, pos=pos, measures=dict(nx.eigenvector_centrality_numpy(DiG)), measure_name="DiGraph Nodes eigenvector centrality")

## 中介中心性（Betweenness Centrality）
def Node_Betweenness_Centrality(G,DiG):
    ## 核心思想是衡量一个节点是不是其他节点联通的必经之地
    ## 计算每2个节点之间的最短路径，如果这些路径很多都经过了某个节点，那么这个节点的重要度比较高
    print(f"无向图的中介中心性：\n{nx.betweenness_centrality(G)}")
    My_Draw(G, pos=pos, measures=dict(nx.betweenness_centrality(G)), measure_name="Graph Nodes betweenness centrality") 

    print(f"有向图的中介中心性：\n{nx.betweenness_centrality(DiG)}")
    My_Draw(DiG, pos=pos, measures=dict(nx.betweenness_centrality(DiG)), measure_name="DiGraph Nodes betweenness centrality")

## 紧密中心性（Closeness Centrality）
def Node_Closeness_Centrality(G,DiG):
    ## 核心思想是衡量一个节点到其他节点的距离，如果一个节点到哪都近，那么这个节点重要度比较高
    ## 计算一个节点到其他所有节点的平均距离
    print(f"无向图的紧密中心性：\n{nx.closeness_centrality(G)}")
    My_Draw(G, pos=pos, measures=dict(nx.closeness_centrality(G)), measure_name="Graph Nodes closeness centrality") 

    print(f"有向图的紧密中心性：\n{nx.closeness_centrality(DiG)}")
    My_Draw(DiG, pos=pos, measures=dict(nx.closeness_centrality(DiG)), measure_name="DiGraph Nodes closeness centrality")

## Katz中心性
def Node_Katz_Centrality(G,DiG):
    ## Katz中心性可以认为是特征向量中心性的一个递进算法，他考虑到了节点间的距离，节点距离越远，其对计算节点重要度的贡献会越小
    print(f"无向图Katz中心性：\n{nx.katz_centrality(G)}")
    My_Draw(G, pos=pos, measures=dict(nx.katz_centrality(G)), measure_name="Graph Nodes Katz centrality")   

    print(f"有向图Katz中心性：\n{nx.katz_centrality(DiG)}")
    My_Draw(DiG, pos=pos, measures=dict(nx.katz_centrality(DiG)), measure_name="DiGraph Nodes Katz centrality")

## PageRank
def Node_PageRank(G,DiG):
    ## PageRank可以认为是Katz中心性的再一次递进，其计算某个节点对当前节点重要度贡献时，又考虑到节点的出度，出度太大的节点重要性贡献会有所惩罚。
    print(f"无向图PageRank：\n{nx.pagerank(G)}")
    My_Draw(G, pos=pos, measures=dict(nx.pagerank(G)), measure_name="Graph Nodes PageRank") 

    print(f"有向图PageRank：\n{nx.pagerank(DiG)}")
    My_Draw(DiG, pos=pos, measures=dict(nx.pagerank(DiG)), measure_name="DiGraph Nodes PageRank")

## HITS算法，Hubs和Authorities
def Node_PageRank(G,DiG):
    ## HITS算法也是用来评价网页重要度的算法
    ## 其核心思想是将网页分为Hubs和Authorities：Hubs可以理解为导航页，会指向很多内容页；Authorities可以认为是内容
    ## HITS算法认为（基本假设）：高质量的Hubs会指向很多高质量的Authorities；反之，高质量的Authorities会被很多高质量Hubs指向
    ## 页面的质量由H值或A值决定，节点的H值是其邻居节点A值之和；节点的A值是其邻居节点的H值之和
    ## 这又是个递归的算法
    H,A = nx.hits(DiG)
    print(f"有向图的HITS_Hubs质量：\n{H}")
    print(f"有向图的HITS_Authorities质量：\n{A}")
    My_Draw(DiG, pos=pos, measures=dict(H), measure_name="DiGraph HITS Hubs") 
    My_Draw(DiG, pos=pos, measures=dict(A), measure_name="DiGraph HITS Authorities") 


if __name__ == "__main__":
    # 导入无向图
    G = nx.karate_club_graph()      # type:nx.Graph
    pos = nx.spring_layout(G,seed=675)
    # 导入有向图
    DiG = nx.DiGraph()
    DiG.add_edges_from([(2,3), (3,2), (4,1), (4,2), (5,2), (5,4), (5,6), (6,2), (6,5),
                        (7,2), (7,5), (8,2), (8,5), (9,2), (9,5), (10,5), (11,5)])
    # ## 节点的邻居
    # Node_Neighbor(G,DiG)
    # ## 节点的度
    # Node_Degree(G,DiG)
    # ## 度中心性（Degree Centrality）
    # Node_Degree_Centrality(G,DiG)
    # ## 特征向量中心性（Eigenvector Centrality）
    # Node_Eigenvector_Centrality(G,DiG)
    # ## 中介中心性（Betweenness Centrality）
    # Node_Betweenness_Centrality(G,DiG)
    # ## 紧密中心性（Closeness Centrality）
    # Node_Closeness_Centrality(G,DiG)
    # ## Katz中心性
    # Node_Katz_Centrality(G,DiG)
    # ## PageRank
    # Node_PageRank(G,DiG)
    # ## HITS算法，Hubs和Authorities
    # Node_PageRank(G,DiG)

    plt.show()
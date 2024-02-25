# 配置环境
import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import matplotlib
print("数据可视化工具包_matplotlib:" + matplotlib.__version__)
import matplotlib.pyplot as plt
# 配置windows 显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

def NetworkX_InnerGraph1():
    # 经典图结构
    fig = plt.figure("NetworkX内置图结构1", figsize=(16, 8), constrained_layout=True)
    plt.suptitle("NetworkX内置图结构1")
    axgrid = fig.add_gridspec(nrows=2,ncols=8)  # 给图分成2行8列的格子，后面的子图可以按需分配格子以分别确定子图像大小

    ## 全连接无向图
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
    
    plt.show()

def NetworkX_InnerGraph2():
    # 栅格图和一些预制图
    fig = plt.figure("NetworkX内置图结构2", figsize=(16, 8), constrained_layout=True)
    plt.suptitle("NetworkX内置图结构2")
    axgrid = fig.add_gridspec(nrows=2,ncols=8)  # 给图分成2行8列的格子，后面的子图可以按需分配格子以分别确定子图像大小

    ## 二维矩形网络图
    G = nx.grid_2d_graph(3,5)
    ax0 = fig.add_subplot(axgrid[0, 0:2])  # 把子图画到前3个格子里
    ax0.set_title("二维矩形网络图")
    nx.draw(G)

    ## 多维矩形网络图
    G = nx.grid_graph(dim=(2,3,4))
    ax1 = fig.add_subplot(axgrid[0, 2:4])
    ax1.set_title("多维矩形网络图")
    nx.draw(G)
    
    ## 二维三角形网络图
    G = nx.triangular_lattice_graph(2,5)  # 三角形的行数和列数
    ax2 = fig.add_subplot(axgrid[0, 4:6])
    ax2.set_title("二维三角形网络图")
    nx.draw(G)
    
    ## 二维六边形网络图
    G = nx.hexagonal_lattice_graph(2,3)  # 六边形的行数和列数
    ax3 = fig.add_subplot(axgrid[0, 6:8])
    ax3.set_title("二维六边形网络图")
    nx.draw(G)
    
    ## n维超立方体网络图
    G = nx.hypercube_graph(4)
    ax4 = fig.add_subplot(axgrid[1, 0:2])
    ax4.set_title("n维超立方体网络图")
    nx.draw(G)
    
    ## 钻石图
    G = nx.diamond_graph()
    ax5 = fig.add_subplot(axgrid[1, 2:4])
    ax5.set_title("钻石图")
    nx.draw(G)
    
    ## 公牛图
    G = nx.bull_graph()
    ax6 = fig.add_subplot(axgrid[1, 4:6])
    ax6.set_title("公牛图")
    nx.draw(G)
    
    ## 房子图
    G = nx.house_graph()
    ax6 = fig.add_subplot(axgrid[1, 6:8])
    ax6.set_title("房子图")
    nx.draw(G)
    
    plt.show()

def NetworkX_InnerGraph3():
    # 其他的一些内置图结构
    fig = plt.figure("NetworkX内置图结构3", figsize=(16, 8), constrained_layout=True)
    plt.suptitle("NetworkX内置图结构3")
    axgrid = fig.add_gridspec(nrows=2,ncols=8)  # 给图分成2行8列的格子，后面的子图可以按需分配格子以分别确定子图像大小

    ## ER随机图
    G = nx.erdos_renyi_graph(10,0.5)  # erdos ranyi 是一个典型的生成随机图的方法
    ax0 = fig.add_subplot(axgrid[0, 0:2])
    ax0.set_title("ER随机图")
    nx.draw(G)

    ## 空手道俱乐部社交网络图
    G = nx.karate_club_graph()  # 这是一个典型的数据
    ax1 = fig.add_subplot(axgrid[0, 2:4])
    ax1.set_title("空手道俱乐部社交网络图")
    pos = nx.circular_layout(G)
    nx.draw(G, pos=pos, with_labels=True)
    
    ## 无标度有向图
    G = nx.scale_free_graph(10)  # 无标度的大致意思是20%的节点占据了80%的边
    ax2 = fig.add_subplot(axgrid[1, 0:2])
    ax2.set_title("无标度有向图")
    nx.draw(G)
    
    ## 雨果《悲惨世界》人物关系图
    G = nx.les_miserables_graph()
    ax3 = fig.add_subplot(axgrid[0:3, 4:8])
    ax3.set_title("雨果《悲惨世界》人物关系图")
    pos = nx.spring_layout(G, seed=10)
    nx.draw(G, pos=pos, with_labels=True)
    
    ## 社群聚类图
    G = nx.caveman_graph(4,3)
    ax4 = fig.add_subplot(axgrid[1, 2:4])
    ax4.set_title("社群聚类图")
    nx.draw(G, with_labels=True)

    plt.show()



if __name__ == '__main__':
    NetworkX_InnerGraph1()
    NetworkX_InnerGraph2()
    NetworkX_InnerGraph3()

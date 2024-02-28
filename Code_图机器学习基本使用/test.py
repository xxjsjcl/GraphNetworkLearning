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

# 将国际象棋对局文件导入成NetworkX图
# 源文件：https://chessproblem.my-free-games.com/PGN/WCC.zip

# 表示对局信息的数据应该被存入有向图的每条边
game_details = ["Event", "Date", "Result", "ECO", "Site"]
def Chess_to_Graph(filePath:str=r'E:\Projects_GitHub\GraphNetworkLearning\Data\案例\WCC.pgn'):
    """
    读取pgn格式的文件转换为nx图。
    返回MultiDiGraph图，节点是选手，边是对局
    """
    G = nx.MultiDiGraph()
    game = {}
    with open(filePath, 'r') as file:
        lines = [line.rstrip("\r\n") for line in file.readlines()]
    for line in lines:
        if line.startswith("["):
            tag, value = line[1:-1].split(" ", 1)
            game[str(tag)] = value.strip('"')
        else:
            # empty line after tag set indicates
            # we finished reading game info
            if game:
                white = game.pop("White")
                black = game.pop("Black")
                G.add_edge(white, black, **game)
                game = {}
    return G
        
        
if __name__ == '__main__':
    G = Chess_to_Graph()


    H = nx.Graph(G) 

    # edge width is proportional number of games played
    edgewidth = [len(G.get_edge_data(u, v)) for u, v in H.edges()]  

    # node size is proportional to number of games won
    wins = dict.fromkeys(G.nodes(), 0.0)
    for u, v, d in G.edges(data=True):
        r = d["Result"].split("-")
        if r[0] == "1":
            wins[u] += 1.0
        elif r[0] == "1/2":
            wins[u] += 0.5
            wins[v] += 0.5
        else:
            wins[v] += 1.0
    nodesize = [wins[v] * 50 for v in H]    

    # Generate layout for visualization
    pos = nx.kamada_kawai_layout(H)
    # Manual tweaking to limit node label overlap in the visualization
    pos["Reshevsky, Samuel H"] += (0.05, -0.10)
    pos["Botvinnik, Mikhail M"] += (0.03, -0.06)
    pos["Smyslov, Vassily V"] += (0.05, -0.03)  

    fig, ax = plt.subplots(figsize=(12, 12))
    # Visualize graph components
    nx.draw_networkx_edges(H, pos, alpha=0.3, width=edgewidth, edge_color="m")
    nx.draw_networkx_nodes(H, pos, node_size=nodesize, node_color="#210070", alpha=0.9)
    label_options = {"ec": "k", "fc": "white", "alpha": 0.7}
    nx.draw_networkx_labels(H, pos, font_size=14, bbox=label_options)   

 
    # Resize figure for label readability
    ax.margins(0.1, 0.05)
    fig.tight_layout()
    plt.axis("off")
    plt.show()
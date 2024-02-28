# 配置环境
## 导入工具包
import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import matplotlib as mpl
print("数据可视化工具包_matplotlib:" + mpl.__version__)
import matplotlib.pyplot as plt
import re  # 正则化表达式工具包
## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['SimHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

# 将美国128城市交通文件导入成NetworkX图
# 源文件，需要解压成txt：https://github.com/networkx/networkx/blob/main/examples/drawing/knuth_miles.txt.gz
def Miles_to_Graph(filePath:str=None):
    """
    将txt文件转换为nx图
    """
    if filePath is None:
        filePath = r'Data\案例\knuth_miles.txt'
    
    with open(filePath, 'r') as file:
        G = nx.Graph()          # 新建一个空的无向图
        G.position = {}         # 增加position字典
        G.population = {}       # 增加population字典
        cities = []             # 保存城市的list

        # 读取文件
        for line in file.readlines():
            if line.startswith('*'):        # '*'开头的为注释
                continue

            numfind = re.compile(r"^\d+")   # 这是一个用于匹配开头时数字的正则表达式
            
            if numfind.match(line):  # 如果开头时数字，这是一行距离行
                dist = line.split()
                for d in dist:
                    G.add_edge(city, cities[i], weight=int(d))
                    i = i + 1
            else:  # 这是一行城市行
                i = 1
                (city, coordpop) = line.split("[")
                cities.insert(0, city)
                (coord, pop) = coordpop.split("]")
                (y, x) = coord.split(",")
                
                G.add_node(city)
                # assign position - Convert string to lat/long
                G.position[city] = (-float(x) / 100, float(y) / 100)
                G.population[city] = float(pop) / 1000
    return G


if __name__ == '__main__':
    G = Miles_to_Graph()
    print('----------查看图的节点和边----------')
    print(G.nodes)
    print(G.edges)

    # 创建一个新图，筛选处距离小于阈值的边
    H = nx.Graph()
    for v in G:
        H.add_node(v)
    for u, v, d in G.edges(data=True):
        if d["weight"] < 500:
            H.add_edge(u, v)
    
    # 可视化
    fig = plt.figure(figsize=(8, 6))
    # 根据度决定颜色，人口数决定大小
    node_color = [float(H.degree(v)) for v in H]
    node_size = [G.population[v] for v in H]
    # 城市位置决定节点位置
    pos = G.position  # 注意pos是个字典，其他的属性是list
    nx.draw(
        G=H,
        pos=G.position,
        node_color = node_color,
        node_size = node_size,
        with_labels = False
    )

    plt.show()

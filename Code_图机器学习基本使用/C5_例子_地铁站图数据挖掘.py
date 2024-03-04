import networkx as nx
print("图工具包_networkx:" + nx.__version__)
import matplotlib as mpl
print("数据可视化工具包_matplotlib:" + mpl.__version__)
import matplotlib.pyplot as plt
import numpy as np
print("数学函数和矩阵运算工具包_numpy:" + np.__version__)
import pandas as pd
print("数据分析和导入工具包_pandas:" + pd.__version__)
import pprint
## 配置windows 显示中文
plt.rcParams['font.sans-serif']=['Microsoft YaHei'] # 用来显示中文标签
plt.rcParams['axes.unicode_minus']=False  # 用来正常显示正负号

# 统一格式的可视化方案
def My_Draw(G, pos, measures:dict, measure_name:str):
    """
    measures: 字典, value值为希望映射到节点颜色的值, key值为需要画的节点
    measure_name:图的名字
    """
    fig = plt.figure(measure_name,figsize=(15,15))
    nodes = nx.draw_networkx_nodes(G, pos=pos, node_size=75, cmap=plt.cm.plasma,
                                   node_color=list(measures.values()),nodelist=measures.keys())
    nodes.set_norm(mpl.colors.SymLogNorm(linthresh=0.01,linscale=1,base=10))
    edges = nx.draw_networkx_edges(G, pos=pos)
    # labels = nx.draw_networkx_labels(G, pos=pos, font_size=9)
    # nx.draw_networkx_labels(G, pos=pos)
    plt.title(measure_name)
    plt.axis('off')
    fig.colorbar(nodes)

# 字典按value排序
def Sorted_Dict_By_Value(dict_input:dict, reverse:bool = True) -> list:
    """
    字典按值排序
    dict_input: 需要排序的字典
    reserve: 是否是从大到小排序
    return: 排序后的字典,但是列表格式,每个元组第一个元素是原字典的key,第二个元素是value
    """
    return sorted(dict_input.items(), key= lambda x:x[1], reverse=reverse)


if __name__=="__main__":
    # 读取地铁站位置表
    filePath = "Data\案例\Shanghai_Metro_Stations.csv"
    df_pos = pd.read_csv(filePath)
    # 读取地铁站连接表
    filePath = "Data\案例\Shanghai_Metro_Lines.csv"
    df_lines = pd.read_csv(filePath)
    print('----------读取地铁站数据----------')
    print(df_pos)
    print(df_lines)
    # 线路颜色表
    metro_line_color_dict = {
        '1':'#EA0B2A',
        '2':'#94D40B',
        '3':'#F8D000',
        '4':'#60269E',
        '5':'#934C9A',
        '6':'#FE6B01',
        '7':'#D80169',
        '8':'#00A0E8',
        '9':'#6FC5E8',
        '10':'#C3A5E1',
        '11':'#792330',
        '12':'#007A61',
        '13':'#F095CE',
        '14':'#827805',
        '15':'#BDA686',
        '16':'#2AD2C5',
        '17':'#B3776C',
        '18':'#D6A361',
        '浦江线':'#9A9A9A'
    }

    # 用连接表创建无向图
    G = nx.Graph()
    pos = {}
    for idx,row in df_pos.iterrows():
        G.add_node(row['站名'])
        pos[row['站名']] = (float(row['x'])/100, float(row['y']/100))

    for idx,row in df_lines.iterrows():
        G.add_edge(row['本站'],row['下站'],Line=row['线路'],Time=row['运行时间'])
    print('----------创建地铁站图----------')
    print(G)
    print(G.edges('人民广场',data=True))

    # 可视化地铁站
    fig = plt.figure("上海地铁站",figsize=(15,15))
    plt.title("上海地铁")
    nx.draw_networkx_nodes(G,pos,node_size=75, node_color='w', edgecolors='black')
    # nx.draw_networkx_labels(G, pos=pos, font_size=9)
    for edge in list(G.edges(data=True)):
        nx.draw_networkx_edges(G,pos, edgelist=[edge], edge_color=metro_line_color_dict[edge[2]['Line']], width=5)


    # 数据挖掘
    print("------------最短路径分析------------------")
    # ## 任意两个节点之间是否存在路径
    # print(f"'沈杜公路'和'复旦大学'之间是否存在路径：{nx.has_path(G,'沈杜公路','复旦大学')}")

    # ## 任意两个节点之间的最短路径，不考虑权重
    # print(f"'沈杜公路'和'复旦大学'之间的最少站点路径长度：{nx.shortest_path_length(G,'沈杜公路','复旦大学')}")
    # print(f"'沈杜公路'和'复旦大学'之间的最少站点最短路径：{nx.shortest_path(G,'沈杜公路','复旦大学')}")

    # ## 任意两个节点之间的最短路径,时间作为权重
    # print(f"'沈杜公路'和'复旦大学'之间的最快时间：{nx.shortest_path_length(G,'沈杜公路','复旦大学',weight='Time')}")
    # print(f"'沈杜公路'和'复旦大学'之间的最快路径：{nx.shortest_path(G,'沈杜公路','复旦大学',weight='Time')}")

    # ## 某一个节点到所有其他节点的最短路径
    # print(f"'复旦大学'到其他站的最短路径长度（站点数）：")
    # pprint.pprint((nx.shortest_path_length(G,source='复旦大学')),width=1)
    # print(f"'复旦大学'到其他站的最短路径（站点数）：{nx.shortest_path(G,source='复旦大学')}")

    # ## 全图平均最短路径长度
    # print(f"'全地铁平均最短路径长度（站点数）：{nx.average_shortest_path_length(G)}")
    # print(f"'全地铁平均最短路径长度（时间）：{nx.average_shortest_path_length(G,weight='Time')}")

    # ## 利用最短路径制作地铁导航系统
    # print("----------地铁导航系统----------")
    # stationA = "昌吉东路"
    # stationB = "同济大学"
    # print(f"从{stationA}到{stationB}的最快线路为：")
    # shortest_path_list = nx.shortest_path(G,source=stationA,target=stationB,weight='Time')
    # for i in range(len(shortest_path_list)-1):
    #     current_station = shortest_path_list[i]     # 当前站
    #     next_station = shortest_path_list[i+1]      # 下站
    #     line_id = G.edges[(current_station,next_station)]['Line']   # 读取线路号
    #     line_time = G.edges[(current_station,next_station)]['Time']   # 读取时间
    #     print(f"{current_station} -> {next_station} , {line_id}号线, {line_time}分钟")
    # print(f"共计{nx.shortest_path_length(G,source=stationA,target=stationB,weight='Time')}分钟")
    # print("------------------------------")


    ## 连接数
    print("------------节点特征分析------------------")
    # print(f"每个站点的度：\n{G.degree()}")
    # print(f"每个站点的度排序：\n{Sorted_Dict_By_Value(dict(G.degree))}")
    # My_Draw(G, pos=pos, measures=dict(G.degree()), measure_name='Degree')
    My_Draw(G, pos=pos, measures=dict(nx.degree_centrality(G)), measure_name='Degree Centrality')
    # # 特征值中心度，可能不收敛
    # print(f"每个站点的Eigenvector Centrality排序：\n{Sorted_Dict_By_Value(nx.eigenvector_centrality(G))}")
    My_Draw(G, pos=pos, measures=dict(nx.eigenvector_centrality(G)), measure_name='Eigenvector Centrality')
    My_Draw(G, pos=pos, measures=dict(nx.betweenness_centrality(G)), measure_name='Betweenness Centrality(必经之地)')
    My_Draw(G, pos=pos, measures=dict(nx.closeness_centrality(G)), measure_name='Closeness Centrality(去哪都近)')
    # My_Draw(G, pos=pos, measures=dict(nx.pagerank(G)), measure_name='PageRank(随机游走)')
    My_Draw(G, pos=pos, measures=dict(nx.katz_centrality(G)), measure_name='Katz Centrality')
    # # HITS Hubs and Authorithies
    # h,a = nx.hits(G)
    # My_Draw(G, pos=pos, measures=h, measure_name='HITS Hubs')
    # My_Draw(G, pos=pos, measures=a, measure_name='HITS Authorithes')


    ## 社群属性分析
    print("------------社群属性分析------------------")
    # print(f"三角形：\n{Sorted_Dict_By_Value(dict(nx.triangles(G)))}")
    # My_Draw(G, pos=pos, measures=dict(nx.triangles(G)), measure_name='三角形')

    # print(f"集群系数：\n{Sorted_Dict_By_Value(dict(nx.clustering(G)))}")
    My_Draw(G, pos=pos, measures=dict(nx.clustering(G)), measure_name='clustering coefficient（集群系数）')






    plt.show()
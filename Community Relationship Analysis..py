import networkx as nx
import matplotlib.pyplot as plt

# 创建一个空的无向图
G = nx.Graph()

# 添加节点
G.add_nodes_from(["Alice", "Bob", "Charlie", "Dave", "Eve"])

# 添加边
G.add_edges_from([("Alice", "Bob"), ("Bob", "Charlie"), ("Charlie", "Dave"), ("Bob", "Dave"), ("Eve", "Dave")])

# 绘制社交网络图
nx.draw(G, with_labels=True, node_color="lightblue", font_weight="bold")

# 分析社区关系
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# 输出节点的度中心性
print("节点的度中心性：")
for node, centrality in degree_centrality.items():
    print(f"{node}: {centrality}")

# 输出节点的介数中心性
print("节点的介数中心性：")
for node, centrality in betweenness_centrality.items():
    print(f"{node}: {centrality}")

# 输出节点的接近中心性
print("节点的接近中心性：")
for node, centrality in closeness_centrality.items():
    print(f"{node}: {centrality}")

# 输出节点的特征向量中心性
print("节点的特征向量中心性：")
for node, centrality in eigenvector_centrality.items():
    print(f"{node}: {centrality}")

# 显示图形
plt.show()

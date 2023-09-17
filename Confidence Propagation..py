import numpy as np
import networkx as nx

# 构建社交网络图
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# 定义节点的观测值
observed_values = {1: 0.8, 2: 0.6, 3: 0.9, 4: None, 5: None}

# 初始化节点的真实值和可信度
true_values = {node: observed_values[node] for node in G.nodes}
confidence_values = {node: 1.0 if observed_values[node] is not None else 0.0 for node in G.nodes}

# 迭代更新真实值和可信度
max_iterations = 10
tolerance = 1e-3
for _ in range(max_iterations):
    previous_true_values = true_values.copy()

    for node in G.nodes:
        if confidence_values[node] > 0.0:
            neighbors = list(G.neighbors(node))
            num_neighbors = len(neighbors)

            if num_neighbors > 0:
                weighted_sum = 0.0
                total_weights = 0.0

                for neighbor in neighbors:
                    weight = confidence_values[neighbor]
                    value = true_values[neighbor] if true_values[neighbor] is not None else 0.5
                    weighted_sum += weight * value
                    total_weights += weight

                true_values[node] = weighted_sum / total_weights
                confidence_values[node] = min(1.0, total_weights / num_neighbors)

    diffs = [abs(true_values[node] - previous_true_values[node]) for node in G.nodes]
    if max(diffs) < tolerance:
        break

# 输出真值估计结果
print("真值估计结果：")
for node in G.nodes:
    print(f"Node {node}: True Value = {true_values[node]}, Confidence = {confidence_values[node]}")

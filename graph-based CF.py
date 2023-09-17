import numpy as np
import networkx as nx

# 创建一个用户评分矩阵
ratings = np.array([
    [5, 3, 0, 0, 4],
    [0, 0, 5, 4, 0],
    [4, 0, 0, 0, 2],
    [0, 0, 4, 3, 1],
    [0, 0, 0, 0, 5],
    [1, 2, 3, 4, 5]
])

# 构建用户图
user_graph = nx.Graph()
num_users = ratings.shape[0]
user_graph.add_nodes_from(range(num_users))
for i in range(num_users):
    for j in range(i + 1, num_users):
        similarity = np.dot(ratings[i], ratings[j]) / (np.linalg.norm(ratings[i]) * np.linalg.norm(ratings[j]))
        user_graph.add_edge(i, j, weight=similarity)

# 根据图结构进行推荐
def graph_based_cf(ratings, user_id, k=2):
    user_neighbors = sorted(user_graph[user_id].items(), key=lambda x: x[1]['weight'], reverse=True)[:k]
    user_ratings = ratings[user_id]
    predicted_ratings = np.zeros(ratings.shape[1])
    for neighbor, edge_data in user_neighbors:
        neighbor_ratings = ratings[neighbor]
        similarity = edge_data['weight']
        predicted_ratings += similarity * neighbor_ratings
    return predicted_ratings / np.sum([edge_data['weight'] for _, edge_data in user_neighbors])

# 示例：对用户0进行电影推荐
user_id = 0
predicted_ratings = graph_based_cf(ratings, user_id)
print("用户 {} 的推荐评分：{}".format(user_id, predicted_ratings))
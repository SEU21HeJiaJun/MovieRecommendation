import numpy as np

# 创建一个电影特征矩阵
movies = np.array([
    [0, 1, 1, 0, 0],  # Movie 1: Action, Adventure
    [1, 0, 0, 1, 0],  # Movie 2: Comedy
    [0, 0, 1, 0, 1],  # Movie 3: Adventure, Sci-Fi
    [1, 0, 0, 0, 1],  # Movie 4: Comedy, Sci-Fi
    [0, 0, 0, 1, 1],  # Movie 5: Sci-Fi
])

# 创建一个用户喜好向量
user_preferences = np.array([0.8, 0.2, 0.7, 0.3, 0.6])  # 用户喜好权重

# 计算电影与用户喜好的相似度
similarities = np.dot(movies, user_preferences)

# 根据相似度进行排序并推荐电影
recommended_movies = np.argsort(similarities)[::-1]  # 降序排列，返回电影索引

# 输出推荐电影
for i in recommended_movies:
    print("推荐电影{}，相似度：{:.2f}".format(i+1, similarities[i]))
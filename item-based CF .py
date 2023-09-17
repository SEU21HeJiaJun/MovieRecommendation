import numpy as np

# 创建一个用户评分矩阵
ratings = np.array([
    [5, 3, 0, 0, 4],
    [0, 0, 5, 4, 0],
    [4, 0, 0, 0, 2],
    [0, 0, 4, 3, 1],
    [0, 0, 0, 0, 5],
    [1, 2, 3, 4, 5]
])

# 计算物品之间的相似度，这里使用余弦相似度
def cosine_similarity(ratings):
    sim = ratings.T.dot(ratings)
    norms = np.array([np.sqrt(np.diagonal(sim))])
    return sim / norms / norms.T

# 根据物品相似度进行推荐
def item_based_cf(ratings, user_id, k=2):
    sim = cosine_similarity(ratings)

    # 获取目标用户的评分
    user_ratings = ratings[user_id]

    # 对目标用户没有评分的物品进行预测评分
    predicted_ratings = np.zeros(ratings.shape[1])
    for i in range(ratings.shape[1]):
        if user_ratings[i] == 0:
            # 只考虑与目标物品相似度最高的k个物品
            top_k_items = np.argsort(sim[i])[::-1][:k]
            predicted_ratings[i] = np.dot(user_ratings, sim[i]) / np.sum(sim[i])

    return predicted_ratings

# 示例：对用户0进行电影推荐
user_id = 0
predicted_ratings = item_based_cf(ratings, user_id)
print("用户 {} 的推荐评分：{}".format(user_id, predicted_ratings))
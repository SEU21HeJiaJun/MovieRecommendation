import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 创建训练数据
train_texts = ["I love this movie",
               "This movie is great",
               "What a fantastic movie",
               "I don't like this movie",
               "This movie is terrible",
               "I hate this movie"]
train_labels = ["positive", "positive", "positive", "negative", "negative", "negative"]

# 创建测试数据
test_texts = ["This movie is amazing",
              "I really enjoy this movie",
              "I can't stand this movie",
              "The movie is awful"]

# 创建特征提取器
vectorizer = CountVectorizer()

# 将文本转换为词频向量
train_features = vectorizer.fit_transform(train_texts)
test_features = vectorizer.transform(test_texts)

# 创建朴素贝叶斯分类器
classifier = MultinomialNB()

# 训练分类器
classifier.fit(train_features, train_labels)

# 进行情感分类预测
predicted_labels = classifier.predict(test_features)

# 输出预测结果
for text, label in zip(test_texts, predicted_labels):
    print("文本：", text)
    print("情感分类：", label)
    print()

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 准备数据
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # 特征数据
y = np.array([6, 15, 24])  # 真值数据

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 在测试集上进行真值估计
y_pred = model.predict(X_test)

# 输出真值估计结果
print("真值估计结果：")
for true_value, predicted_value in zip(y_test, y_pred):
    print(f"True Value: {true_value}, Predicted Value: {predicted_value}")

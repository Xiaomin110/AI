"""
    使用numpy实现Boston房价预测
    Step1 数据加载，来源sklearn中的load_boston
    Step2 数据规范化，将X 采用正态分布规范化
    Step3 初始化网络
    Step4 定义激活函数，损失函数，学习率 epoch
    Step5 循环执行：前向传播，计算损失函数，反向传播，参数更新
    Step6 输出训练好的model参数，即w1, w2, b1, b2
""" 
import numpy as np
from sklearn.datasets import load_boston
from sklearn.utils import shuffle, resample

# 数据加载
data = load_boston()
X_ = data['data']
y = data['target']
# 将y转化为矩阵的形式
y = y.reshape(y.shape[0],1)

# 数据规范化
X_ = (X_ - np.mean(X_, axis=0)) / np.std(X_, axis=0)

"""
    初始化网络参数
    定义隐藏层维度，w1,b1,w2,b2
""" 
n_features = X_.shape[1]
n_hidden = 10
w1 = np.random.randn(n_features, n_hidden)
b1 = np.zeros(n_hidden)
w2 = np.random.randn(n_hidden, 1)
b2 = np.zeros(1)

# relu函数
def Relu(x):
    """ 这里写你的代码 """
    pass


# 设置学习率
learning_rate = 1e-6

# 定义损失函数
def MSE_loss(y, y_hat):
    """ 这里写你的代码 """
    pass

# 定义线性回归函数
def Linear(X, W1, b1):
    """ 这里写你的代码 """
    pass

# 5000次迭代
for t in range(5000):
    # 前向传播，计算预测值y (Linear->Relu->Linear)
    """ 这里写你的代码 """


    # 计算损失函数, 并输出每次epoch的loss
    """ 这里写你的代码 """


    # 反向传播，基于loss 计算w1和w2的梯度
    """ 这里写你的代码 """    


    # 更新权重, 对w1, w2, b1, b2进行更新
    """ 这里写你的代码 """    


# 得到最终的w1, w2
print('w1={} \n w2={}'.format(w1, w2))

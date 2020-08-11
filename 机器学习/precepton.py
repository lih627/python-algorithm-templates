"""
线性可分感知机对偶形式代码
"""

import numpy as np
import random


class Perceptron(object):
    def __init__(self,
                 max_iter=5000,
                 eta=1,
                 ):
        self.eta = eta
        self.max_iter_ = max_iter
        self.w = 0

    def fit(self, X, y):
        """
        X: [k, n]
        y: [k, ]
        compute w:[n + 1,]
        """
        # [1, k]
        self.alpha = np.zeros([1, X.shape[0]])
        n_iter_ = 0
        # [k, n + 1]
        Extend_X = np.hstack([X, np.ones([X.shape[0], 1])])
        # [k, k]
        self.Gram = Extend_X.dot(Extend_X.T)
        while n_iter_ < self.max_iter_:
            index = random.randint(0, y.shape[0] - 1)
            # \sum(\alpha x y_i x x_i x x_j)
            pred = self.alpha.dot(np.multiply(y, self.Gram[index, :]))
            # y_j x pred
            if y[index] * pred <= 0:
                self.alpha[0, index] += self.eta
            n_iter_ += 1
        # 恢复扩充权重向量
        self.w = self.alpha.dot(np.multiply(y, Extend_X.T).T)

    def predict(self, X):
        X = np.hstack([X, np.ones(X.shape[0]).reshape((-1, 1))])
        rst = np.array([1 if rst else -1 for rst in np.dot(X, self.w.T) > 0])
        return rst

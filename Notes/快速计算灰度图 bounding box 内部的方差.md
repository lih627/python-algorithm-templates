# [CV] 快速计算灰度图 bounding box 内部的方差

## 简介

给定一张灰度图和一系列 bounding boxes，每个bounding box(bbox) 通过 `[left, top, right, down]` 编码，计算每个 `bbox` 内部像素的均值和方差。

直观的思路是对每个`bbox`计算均值然后计算方差，每一个的时间复杂度为$O(k\cdot w\cdot h)$ 其中 $k$ 是一个常量。当 `bbox` 很多的时候，时间复杂度过高。 计算方差肯定绕不过均值，先思考如何快速计算均值。

## Haar 特征

本科的时候学过 `VJ-Detector`，具体原理已经忘掉了，但记得有一个haar可以快速计算区域内像素质和。思路类似二维前缀和。

```
-------------------y
|
|    A-------B
|    |       |
|    |       |
|.   C-------D
|
x
```

如图，我们定义:

$$
\begin{equation}
haar(x, y) = \sum_{i = 0}^{x}\sum_{j = 0}^{y}I(i, j)
\end{equation}
$$

那么图中`A, B, C, D`构成的面积可以表达为

```
sum_ = haar[Dx][Dy] - haar[Bx - 1][By] - haar[Cx][Cy - 1] - haar[Ax - 1][Ay - 1]
```

同时像素的个数可以被表达为

```
area = (D_x - A_x + 1) * (D_y - D_y + 1)
```

这样构造好了`haar`以后，能够很快的计算出均值，代码如下，没有经过测试，但是原理是没有问题的:

```python
def mean_(img, bboxes):
    # bboxes 为bbox 构成的列表，bbox通过[left top right down] 编码
    if len(img) == 0:
        return None
    row, col = len(img), len(img[0])
    haar = [img[i][:] for i in range(row)]
    # 构造积分图
    for i in range(row):
        for j in range(col):
            if i == 0:
                haar[i][j] += haar[i][j - 1] if j > 0 else 0
            elif j == 0:
                haar[i][j] += haar[i - 1][j]
            else:
                haar[i][j] += haar[i - 1][j] + haar[i][j - 1] - haar[i - 1][j - 1]
    n_bboxes = len(bboxes)
    mean_ = [0] * n_bboxes
    for idx, bbox in enumerate(bboxes):
        A = bbox[:2]
        B = bbox[3:]
        C = [A[0], B[1]]
        D = [B[0], A[1]]
        area = (bbox[2] - bbox[0] + 1) * (bbox[3] - bbox[1] + 1)
        sum_ = 0
        if bbox[0] == 0 and bbox[1] == 0:
            sum_ = haar[D[1]][D[0]]
        elif bbox[0] == 0:
            sum_ = haar[D[1]][D[0]] - haar[B[1] - 1][B[0]]
        elif bbox[1] == 0:
            sum_ = haar[D[1]][D[0]] - haar[C[1]][C[0] - 1]
        else:
            sum_ = haar[D[1]][D[0]] - haar[B[1] - 1][B[0]] - haar[C[1]][C[0] - 1] + haar[A[1] -1][A[0] - 1]
        mean_[idx] = sum_ / float(area)
    return mean_
```



## 快速计算方差

首先考虑一下方差的公式
$$
\begin{equation}
\sigma^2=\frac{1}{n}\sum_{i}\left(x_i - \bar{x}\right)^2
\end{equation}
$$
展开
$$
\begin{equation}
\frac{1}{n}\sum_{i}\left(x_i - \bar{x}\right)^2\\
=\frac{1}{n}\sum_{i}(x_i^2 - 2x_i\bar{x} + \bar{x})^2\\
=\frac{1}{n}\sum_{i}\left\{(x_i^2) - 2\cdot(x_i\cdot \bar{x} + \bar{x}^2)\right\}\\
= E(X^2) - 2\bar{x}E(X) + E(X)^2\\
=E(X^2) - E(X)^2  
\end{equation}
$$
​	所以只需要再对 $X^2$ 构造积分图就可以了。
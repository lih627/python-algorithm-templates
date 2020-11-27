# LeetCode 1074 元素为目标值的子矩阵数量

## 题目

> 给出矩阵 `matrix` 和目标值 `target`，返回元素总和等于目标值的非空子矩阵的数量。
>
> 子矩阵 `x1, y1, x2, y2` 是满足 `x1 <= x <= x2` 且 `y1 <= y <= y2` 的所有单元 matrix[x][y] 的集合。
>
> 如果 `(x1, y1, x2, y2)` 和 `(x1', y1', x2', y2')` 两个子矩阵中部分坐标不同 （如：x1 != x1'），那么这两个子矩阵也不同。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/number-of-submatrices-that-sum-to-target
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



## 思路一 前缀和

定义`row` 和`col` 分别对应矩阵的行数和列数。

一个直观的思路是使用前缀和。定义$prefix[x][y]$ 表示从 `[0, 0]` 到`[x, y]` 的自矩阵元素综合
$$
prefix[x][y]=\sum_{i=0}^x\sum_{j=0}^{y}matrix[x][y]
$$
生成此矩阵需要$O(row\cdot col)$ 时间复杂度，基于如下递推公式：
$$
prefix[x][y] = matrix[x][y] + prefix[x-1][y] +\\ prefix[x][y -1] -prefix[x- 1][y - 1]
$$
生成前缀和矩阵后，可以在 $O(1)$ 时间内计算任意子矩阵元素和
$$
ret[i, j, x, y] = prefix[x][y] -prefix[i - 1][y] \\-prefix[x][j - 1] + prefix[i - 1][j - 1]
$$
`[i, j, x, y]` 表示起始坐标是`[i, j]`， 中止坐标`[x, y]` 注意这两个公式都需要考虑一下边界条件。

那么思路是枚举每一对起始和终止坐标，时间复杂度为$O(row^2\cdot col^2)$

实测大概是 600ms，代码如下，注意边界处理

```c++
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int row = matrix.size(), col = matrix[0].size();
        int prefix[row][col];
        memset(prefix, 0, sizeof(prefix));
        int ret = 0;
        for(int x = 0; x < row; ++x){
            for(int y = 0; y < col; ++y){
                if (x == 0 && y == 0){
                    prefix[x][y] = matrix[x][y];
                }
                else if(x == 0){
                    prefix[x][y] = matrix[x][y] + prefix[x][y - 1];
                }
                else if(y == 0){
                    prefix[x][y] = matrix[x][y] + prefix[x - 1][y];
                }
                else prefix[x][y] = matrix[x][y] + prefix[x - 1][y] + prefix[x][y - 1] - prefix[x - 1][y - 1];
                for (int i = 0; i <= x; ++ i){
                    for(int j = 0; j <= y; ++j){
                        int c =  i && j ? prefix[i - 1][j - 1]: 0;
                        int a = i ? prefix[i - 1][y]: 0;
                        int b = j ? prefix[x][j - 1]: 0;
                        int tmp = prefix[x][y] - a - b + c;
                        if (tmp == target) ++ ret;
                    }
                }
            }
        }
        return ret;
    }
};
```

## 思路二 前缀和+哈希表优化

定义一维前缀和矩阵 `prefix`，对应每一列元素的前缀和
$$
prefix[x][y] = \sum_{i}^xmatrix[i][y]
$$
那么通过哈希表可以在$O(col)$ 时间内计算某两行之间符合要求的子矩阵数量。过程如下：

1. 选取两行`r1, r2`
2. 创建哈希表`counter[k] = v`分别为前缀和和出现次数 `counter[0] = 1`
3. 记录前缀和`cSum = 0`, 初始化符合要求的子矩阵计数`ret = 0`
4. 枚举 `c = 0,...col`
   1. `cSum += prefix[r2][c] - prefix[r1 - c][c]`
   2. `ret += counter[cSum - target]`
   3. `counter[cSum] += 1`

在这种情况下，总体上需要枚举所有的起始和终止行，时间复杂度为 $O(row^2\cdot col)$



代码如下，用时约1800ms，原因在于哈希表在内循环结束后需要清空。

```c++
class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int row = matrix.size(), col = matrix[0].size();
        int accRow[row][col];
        memset(accRow, 0, sizeof(accRow));
        for(int i = 0; i < row; ++i)
            for(int j = 0; j < col; ++j){
                if (i == 0) accRow[i][j] = matrix[i][j];
                else accRow[i][j] = matrix[i][j] + accRow[i - 1][j];
            }
        
        unordered_map<int, int> preSumCnt;
        int ret = 0;
        preSumCnt[0] = 1;
        for(int sr = 0; sr < row; ++sr){
            for(int er = sr; er < row; ++er){
                int cSum = 0;
                for(int c = 0; c < col; ++c){
                    cSum += accRow[er][c] - (sr? accRow[sr - 1][c]: 0);
                    ret += preSumCnt[cSum - target];
                    ++preSumCnt[cSum];
                }
                preSumCnt.clear(); //此处时间复杂度较高
                preSumCnt[0] = 1;
            }
        }
        return ret;
    }
};
```

可以通过手写哈希表来优化，参考 oi.wiki的代码，实测约 90ms。这里有点调参的意思，选取 97 作为哈希函数参数时，总共映射的 key 不超过 97 * 4 个。每个循环中清空哈希表的耗时会小很多。

```c++
const int SZ = 97;

struct hash_map {  // 哈希表模板

  struct data {
    long long u;
    int v, nex;
  };                // 前向星结构
  
  data e[SZ << 2];  // SZ 是 const int 表示大小 调参
  int h[SZ], cnt;
  int hash(long long u) {
      int ret = u % SZ; 
      return ret > -1? ret: ret + SZ; 
      }

  int& operator[](long long u) {
    int hu = hash(u);  // 获取头指针
    for (int i = h[hu]; i; i = e[i].nex)
      if (e[i].u == u) return e[i].v;
    return e[++cnt] = (data){u, 0, h[hu]}, h[hu] = cnt, e[cnt].v;
  }

  void clear(){
      cnt = 0;
      memset(h, 0, sizeof(h));
  }
  hash_map() {
    cnt = 0;
    memset(h, 0, sizeof(h));
  }
};


class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int row = matrix.size(), col = matrix[0].size();
        int prefix[row][col];
        memset(prefix, 0, sizeof(prefix));
        for (int i = 0; i < row; ++i)
            // O(row * col)
            for(int j = 0; j < col; ++j){
                prefix[i][j] = matrix[i][j] + (i? prefix[i - 1][j]: 0);
            }
        int ret = 0;
        hash_map mp;
        mp[0] = 1;
        for (int sr = 0; sr < row; ++sr){
            for(int er = sr; er < row; ++er){
                int cSum = 0;
                for(int c = 0; c < col; ++c){
                    cSum += prefix[er][c] - (sr? prefix[sr - 1][c]: 0);
                    ret += mp[cSum - target];
                    ++mp[cSum]; 
                }
                mp.clear();
                mp[0] = 1;
            }
        }
        return ret;
    }
};
```


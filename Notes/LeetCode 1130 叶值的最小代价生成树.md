# LeetCode 1130 叶值的最小代价生成树

[toc]

## 题目

给你一个正整数数组 `arr`，考虑所有满足以下条件的二叉树：

- 每个节点都有 0 个或是 2 个子节点。

- 数组 `arr` 中的值与树的中序遍历中每个叶节点的值一一对应。（知识回顾：如果一个节点有 0 个子节点，那么该节点为叶节点。）

- 每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。

在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。  

```
输入：arr = [6,2,4]
输出：32
解释：
有两种可能的树，第一种的非叶节点的总和为 36，第二种非叶节点的总和为 32。

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
```

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 思路

区间DP，定义`dp(i, j)` 为数组从`i` 到`j`区间生成二叉树非叶子结点的最小可能总和，那么有
$$
dp[i][j] = \min_{i\le k\le j}\left\{dp[i][k] + dp[k][j] + \max_{i\le p\le k} node[p] \cdot\max_{k\le q\le j}node[q] \right\} 
$$
即要保留左子树区间和右子树区间的最小值的同时，加上新生成的根结点的值。根结点的值是左子树和右子树结点最大值的乘积。

那么可以采用记忆话递归的思路，首先定义备忘路数组$memo[i][j][0]$ 表示区间内二叉树的最小总和`memo[i][j][1]` 表示区间内结点的最大值。

代码如下

```cpp
int memo[45][45][2];

class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        memset(memo, -1, sizeof(memo));
        int ret = dp(0, arr.size() - 1,  arr);
        return ret;
    }

    int dp(int i, int j, vector<int> &arr){

        if(memo[i][j][0] != -1) return memo[i][j][0];
        if (i > j){
            memo[i][j][0] = 0;
            memo[i][j][1] = 0;
            return memo[i][j][0];
        }
        if (i == j){
            memo[i][j][0] = 0;
            memo[i][j][1] = arr[i];
            return memo[i][j][0];
        }
        if(i + 1 == j){
            memo[i][j][0] = arr[i] * arr[j];
            memo[i][j][1] = max(arr[i], arr[j]);
            return memo[i][j][0];
        }
        int ret = dp(i + 1, j, arr) + arr[i] * memo[i + 1][j][1];
        memo[i][j][1] = max(arr[i], memo[i + 1][j][1]);
        if (dp(i, j - 1, arr) + arr[j] * memo[i][j - 1][1] < ret){
            ret = dp(i, j - 1, arr) + arr[j] * memo[i][j - 1][1] ;
            memo[i][j][1] = max(arr[j], memo[i][j - 1][1]);
        }
        for (int k = i + 1; k + 1< j; ++k){
            int left = dp(i, k, arr), right = dp(k + 1, j , arr);
            if (left + right + memo[i][k][1] * memo[k + 1][j][1] < ret){
                ret = left + right + memo[i][k][1] * memo[k + 1][j][1];
                memo[i][j][1] = max(memo[i][k][1], memo[k + 1][j][1]);
            }
        }
        memo[i][j][0] = ret;
        return memo[i][j][0];
    }
};
```


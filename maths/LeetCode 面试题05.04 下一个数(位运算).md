# LeetCode 面试题05.04 下一个数(位运算)

[toc]

> 题解参考:
>
> [github 代码](https://gist.github.com/weirenw/5252255)
>
> [LeetCode题解代码](https://leetcode-cn.com/problems/closed-number-lcci/solution/wei-yun-suan-nb-by-hei-ye-3/)
>
> [集合中的位运算](https://blog.csdn.net/xushao_Movens/article/details/52199157)



## 题目

题目来自[LeetCode 面试题05.04](https://leetcode-cn.com/problems/closed-number-lcci/)

> 下一个数。给定一个正整数，找出与其二进制表达式中 1 的个数相同且大小最接近的那两个数（一个略大，一个略小）。
>
> ```
> 示例 1: 
> 输入：num = 2（或者0b10）
> 输出：[4, 1] 或者（[0b100, 0b1]）
> 示例 2:
> 输入：num = 1
> 输出：[2, -1]
> ```
>
>
> 提示:
>
> num 的范围在 `[1, 2147483647]` 之间；
> 如果找不到前一个或者后一个满足条件的正数，那么输出 ``-1`。
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/closed-number-lcci
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

## 思路

一种思路是从右到左(从低位到高位)找到二进制中的`01` 和`10` 模式，其中`0`和`1`互换后从高位到低位按顺序填充剩下的`0` 和 `1` 就可以了。

```
0101
next: 0110
prev: 0011
```

可以通过一些循环的判定来解决，参照我写的[这片题解](https://leetcode-cn.com/problems/closed-number-lcci/solution/python-wei-yun-suan-mei-you-shi-yong-zi-fu-chuan-d/)

```python
class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:

        def findLarger(n):
            num_digits = num_zeros = num_ones = 0
            find_01 = False
            while n:
                num_digits += 1
                if n & 1:
                    num_ones += 1
                else:
                    num_zeros += 1
                    if num_ones:
                        n >>= 1
                        find_01 = True
                        break
                n >>= 1
            if find_01:
                n <<= 1
                n += 1
                for i in range(num_zeros):
                    n <<= 1
                for i in range(num_ones - 1):
                    n <<= 1
                    n += 1
                return n
            else:
                if num_ones == 1:
                    return 1 << num_digits
                else:
                    res = 2
                    for i in range(num_ones - 1):
                        res <<= 1
                        res += 1
                    return res

        def findSmaller(n):
            num_digits = num_ones = num_zeros = 0
            find_10 = False
            while n:
                num_digits += 1
                if not n & 1:
                    num_zeros += 1
                else:
                    num_ones += 1
                    if num_zeros:
                        find_10 = True
                        n >>= 1
                        break
                n >>= 1
            if find_10:
                n <<= 1
                for i in range(num_ones):
                    n <<= 1
                    n += 1
                for i in range(num_zeros - 1):
                    n <<= 1
                return n
            else:
                return -1

        return [findLarger(num), findSmaller(num)]
```

但是从评论区看到了另外的有意思的思路，其表示为集合的K元素子集。

例如含有4个元素的所有子集为：

```
00001111
00010111
00011011
....
11110000
```

元素满足从小到大生成。以`00010111 -> 00011011`为例子：

1. 求出最低位的1开始的连续的1的区间`0001 0111 -> 00000 0111`
2. 将此区间全部变成0，并将区间左侧的0变成1 `0001 0111 -> 0001 1000`
3. 将第1步去除的区间右移，直到剩下的1的个数减少一个`0000 0111 -> 0000 0011`
4. 将第2步和第3步的结果或操作 `0001 1000 | 0000 0011 -> 0001 1011`

```python
def getlarge(n):
    tmp = n & (-n)
    '''
    tmp 为 lowbit 找到从右边开始第一个1的位置
    e.g. 1110 1100 & 0001 0100 = 0000 0100
    '''
    initialbig = n + tmp
    '''
    将第 1 个 1 往高 bit 位置移动
    实现步骤 2
    e.g. 1110 1100 + 0000 0100 = 1111 0000
    '''
    lowpart = ((n & (~initialbig)) // tmp) >> 1
    '''
    完成步骤 3
    首先要找到第一步的区间
    1110 1100 对应 0000 1100 (n & (~initialbig))
    首先让1移动到最右边 因此除 tmp
    然后在向右移动 1 位即可
    e.g. 1110 1100 & 0000 1111 = 0000 1100
         0000 1100 / 0000 0100 = 0000 0011
    '''
    ans = initialbig | lowpart
    return ans
```

取反的下一个数再取反就是上一个数。

例如`N = 1110 1100` 需要找到第一个在0左侧的1的位置。然后交换他们。 `getlarge` 实现找到第一个在1左侧的0，交换他们，并且把剩下的1比特放在末尾。那么`~N = 1 0001 0011` 使用`getlarge`函数，得到 `1 0010 0011`，取反后 `0 1101 1100` 正是最后的结果。

最终代码如下：

```python
class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        def getlarger(n):
            tmp = n & -n
            initialbig = tmp + n
            lowpart = ((n & ~initialbig) // tmp) >> 1
            return lowpart | initialbig
        return [2, -1] if num == 1 else [getlarger(num), ~getlarger(~num)]
```




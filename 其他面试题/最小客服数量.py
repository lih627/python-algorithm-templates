"""
携程 2020 面试题

携程呼叫中心 7×24 小时帮助旅客解决在途中的各种问题，
为了尽可能提升服务质量，公司希望客服人数可以满足所有旅
客的来电，不用排队等待人工客服。现在提供客服中心所有的通
话记录时间，你能算出最少需要多少名客服吗？

输入
输入一个 n 表示要输入的通话记录个数，
接下来输入 n 行，每行为逗号相隔的两个整数，
两个数字分别代表呼入时间和挂断时间的时间戳。
举例：10,30，表示 [10,30)，代表第 10 秒呼入，
第 30 秒已经挂断，即第 30 秒可以接入新的来电；
每一行都是一条通话记录，通话记录已经按呼入时间由小到大排序；

输出
输出一个整数；代表最少需要多少客服，可以满足所有旅客来电不用等待。

样例输入
6
0,30
0,50
10,20
15,30
20,50
20,65

样例输出
5
"""


def solve(n, times):
    """
    小根堆/优先队列
    """
    if n == 0:
        return 0
    import heapq
    heap = []
    heapq.heappush(heap, times[0][1])
    for time in times[1:]:
        if time[0] >= heap[0]:
            # 不需要新的客服
            heapq.heappop(heap)
        heapq.heappush(heap, time[1])
    print(heap)
    return len(heap)


if __name__ == '__main__':
    n = int(input())
    times = []
    for i in range(n):
        times.append(list(map(int, input().split(','))))
    print(times)
    print(solve(n, times))

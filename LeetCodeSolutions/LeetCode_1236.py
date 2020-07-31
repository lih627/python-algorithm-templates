#
# @lc app=leetcode.cn id=1236 lang=python3
#
# [1236] 网络爬虫
#

# @lc code=start
# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
# class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        split_url = startUrl.split('/')
        host_name = '//'.join([split_url[0], split_url[2]])
        visited = set([startUrl])
        from collections import deque
        que = deque()
        que.append(startUrl)
        while que:
            curl = que.popleft()
            cret = htmlParser.getUrls(curl)
            for item in cret:
                if item[:len(host_name)] == host_name and item not in visited:
                    que.append(item)
                    visited.add(item)
        return list(visited)
# @lc code=end

#
# @lc app=leetcode.cn id=1242 lang=python3
#
# [1242] 多线程网页爬虫
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
from typing import List
import threading
import queue


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        split_url = startUrl.split('/')
        host_name = '//'.join([split_url[0], split_url[2]])
        self.result_queue = queue.Queue()
        self.task_queue = queue.Queue()
        self.parser = htmlParser
        self.task_queue.put(startUrl)
        print(host_name)
        visited = set([startUrl])
        for i in range(5):
            t = threading.Thread(target=self._crawl)
            t.daemon = True
            t.start()
        running = 1
        host_name_len = len(host_name)
        while running > 0:
            ret_url = self.result_queue.get()
            for item in ret_url:
                if item[:host_name_len] == host_name and item not in visited:
                    self.task_queue.put(item)
                    visited.add(item)
                    running += 1
            running -= 1
        return list(visited)

    def _crawl(self):
        while True:
            url = self.task_queue.get()
            ret = self.parser.getUrls(url)
            self.result_queue.put(ret)

# @lc code=end

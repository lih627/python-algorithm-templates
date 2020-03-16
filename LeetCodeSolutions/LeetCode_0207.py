class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0] * numCourses
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        que = collections.deque()

        for course, indegree in enumerate(indegrees):
            if not indegree:
                que.append(course)

        cnt = numCourses
        while que:
            course = que.popleft()
            cnt -= 1
            for tmp in adjacency[course]:
                indegrees[tmp] -= 1
                if not indegrees[tmp]:
                    que.append(tmp)
        return not cnt

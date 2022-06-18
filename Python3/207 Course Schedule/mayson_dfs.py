class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 1:
            return True
        graph = [[] for i in range(numCourses)]
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
        visit = [0] * numCourses  # 0 = unknown, 1 = visiting, 2 = visited

        # cycle = False
        def dfs(node):
            if visit[node] == 2:
                return True
            if visit[node] == 1:
                return False
            visit[node] = 1
            for v in graph[node]:
                if not dfs(v):
                    return False
            visit[node] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

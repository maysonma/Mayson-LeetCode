class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        graph_l = [[] for _ in range(numCourses)]
        for edge in prerequisites:
            graph_l[edge[1]].append(edge[0])
        visit = [0] * numCourses  # 0 = unknown, 1 = visiting, 2 = visited
        ans = []

        # cycle = False
        def dfs(node):
            if visit[node] == 1:
                return False
            if visit[node] == 2:
                return True
            visit[node] = 1
            for v in graph_l[node]:
                if not dfs(v):
                    return False
            visit[node] = 2
            ans.append(node)
            return True

        for v in range(numCourses):
            if not dfs(v):
                return []
        return list(reversed(ans))

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        if n < 1:
            return False
        visited = [0] * n
        adj_list = rooms

        def dfs(node):
            nonlocal visited
            if visited[node]:
                return
            visited[node] = 1
            for v in adj_list[node]:
                dfs(v)

        dfs(0)
        return all(visited)

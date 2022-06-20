from collections import deque
from typing import List


class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        # graph = {i: [] for i in range(1, n+1)}
        # in_degrees = {i: 0 for i in range(1, n+1)}
        graph = {}
        in_degrees = {}
        for seq in sequences:
            for num in seq:
                graph[num] = []
                in_degrees[num] = 0

        if len(nums) > len(graph):
            return False

        for seq in sequences:
            for i in range(len(seq) - 1):
                u, v = seq[i], seq[i + 1]
                graph[u].append(v)
                in_degrees[v] += 1

        sources = deque()
        for v, d in in_degrees.items():
            if d == 0:
                sources.append(v)

        sorted_order = []
        while sources:
            if len(sources) > 1:
                return False
            u = sources.popleft()
            sorted_order.append(u)
            for v in graph[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    sources.append(v)

        if len(sorted_order) != len(nums):
            return False
        else:
            for i, j in zip(sorted_order, nums):
                if i != j:
                    return False
        return True

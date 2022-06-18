from collections import deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        in_degrees = {}
        for word in words:
            for character in word:
                graph[character] = []
                in_degrees[character] = 0
        vertices = len(graph)

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            same = True
            for i in range(min(len(w1), len(w2))):
                c1, c2 = w1[i], w2[i]
                if c1 != c2:  # c1 --> c2
                    same = False
                    graph[c1].append(c2)
                    in_degrees[c2] += 1
                    break
            if same:
                if len(w1) > len(w2):
                    return ""

        sorted_order = []
        sources = deque()
        for u, d in in_degrees.items():
            if d == 0:
                sources.append(u)

        while sources:
            u = sources.popleft()
            sorted_order.append(u)
            for v in graph[u]:
                in_degrees[v] -= 1
                if in_degrees[v] == 0:
                    sources.append(v)

        if len(sorted_order) == vertices:
            return ''.join(sorted_order)
        else:
            return ""

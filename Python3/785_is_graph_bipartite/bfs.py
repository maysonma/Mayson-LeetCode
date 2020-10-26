from typing import List


class BreadthFirstSearch:
    def __init__(self):
        pass

    def driver(self, graph: List[List[int]]):
        n = len(graph)
        seen = [0] * n
        self._driver_init()
        for i in range(n):
            if not seen[i]:
                pass

    def _driver_init(self):
        pass

    def _driver_cleanup(self):
        pass

    def bfs(self, graph, s):
        # Initialization
        self._init(graph, s)


    def _init(self, graph, s):
        pass

    def _visit(self, v, u):
        pass

    def _previsit(self, v, u):
        pass

    def _postvisit(self, u):
        pass

    def _cleanup(self, graph):
        pass
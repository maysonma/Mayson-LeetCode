"""
# Definition for a Node.
"""
from collections import deque


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return
        node_dict = {}
        Q = deque()
        Q.append(node)
        dup = Node(node.val, [])
        node_dict[node] = dup
        while Q:
            vertex = Q.popleft()
            for neighbor in vertex.neighbors:
                if neighbor not in node_dict:
                    neighbor_dup = Node(neighbor.val, [])
                    node_dict[neighbor] = neighbor_dup
                    vertex.neighbors.append(neighbor_dup)
                    Q.append(neighbor)
                else:
                    vertex.neighbors.append(node_dict[neighbor])
        return dup


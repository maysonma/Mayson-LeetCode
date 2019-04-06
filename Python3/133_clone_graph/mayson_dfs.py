"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_dict = {}

        def dfs(node):
            nonlocal node_dict
            if node is None:
                return None
            if node in node_dict:
                return node_dict[node]
            else:
                duplicate = Node(node.val, [])
                node_dict[node] = duplicate
                for neighbor in node.neighbors:
                    duplicate.neighbors.append(dfs(neighbor))
                return duplicate

        return dfs(node)

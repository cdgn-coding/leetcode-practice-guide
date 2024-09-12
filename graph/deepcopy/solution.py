# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        stack = [node]
        nodes = {}
        visited = set()
        adj = set()

        # Create copy of nodes with DFS
        while stack:
            current = stack.pop()
            # Prevent cycles, this is a connected graph, not necessarily a tree
            if current.val in visited:
                continue
            visited.add(current.val)

            # Create the copy
            nodes[current.val] = Node(current.val)
            for neighbor in current.neighbors:
                adj.add((current.val, neighbor.val))
                stack.append(neighbor)

        # Connect nodes
        for val1, val2 in adj:
            # Connect both ways, this is an undirected graph
            nodes[val1].neighbors.append(nodes[val2])

        return nodes[node.val]


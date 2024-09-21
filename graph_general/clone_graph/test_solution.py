import unittest
from typing import List

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class TestCloneGraph(unittest.TestCase):
    def test_example1(self):
        # Create the original graph
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node1, node3]

        # Clone the graph
        cloned = Solution().cloneGraph(node1)

        # Check if the cloned graph has the same structure
        self.assertEqual(cloned.val, 1)
        self.assertEqual(len(cloned.neighbors), 2)
        self.assertEqual(cloned.neighbors[0].val, 2)
        self.assertEqual(cloned.neighbors[1].val, 4)
        self.assertEqual(cloned.neighbors[0].neighbors[0].val, 1)
        self.assertEqual(cloned.neighbors[0].neighbors[1].val, 3)
        self.assertEqual(cloned.neighbors[1].neighbors[0].val, 1)
        self.assertEqual(cloned.neighbors[1].neighbors[1].val, 3)

    def test_example2(self):
        # Create the original graph (single node)
        node = Node(1)

        # Clone the graph
        cloned = Solution().cloneGraph(node)

        # Check if the cloned graph is correct
        self.assertEqual(cloned.val, 1)
        self.assertEqual(len(cloned.neighbors), 0)

    def test_example3(self):
        # Test with empty graph
        self.assertIsNone(Solution().cloneGraph(None))

    def test_large_graph(self):
        # Create a larger graph
        nodes = [Node(i) for i in range(1, 101)]
        for i in range(100):
            nodes[i].neighbors = [nodes[(i+1)%100], nodes[(i+2)%100]]

        # Clone the graph
        cloned = Solution().cloneGraph(nodes[0])

        # Check if the cloned graph has the correct structure
        visited = set()
        stack = [cloned]
        while stack:
            node = stack.pop()
            if node.val not in visited:
                visited.add(node.val)
                self.assertEqual(len(node.neighbors), 2)
                self.assertIn(node.neighbors[0].val, [(node.val % 100) + 1, (node.val % 100) + 2])
                self.assertIn(node.neighbors[1].val, [(node.val % 100) + 1, (node.val % 100) + 2])
                stack.extend(node.neighbors)
        self.assertEqual(len(visited), 100)

if __name__ == '__main__':
    unittest.main()
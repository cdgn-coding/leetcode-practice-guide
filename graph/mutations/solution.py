# AACCGGTT
# Generate mutations in order left to right
# Add to the queue
# Get from the queue, check if valid
# Why queue?
# We want shortest path
# So we use BFS, this way first path to reach the end is obtained

# iteration 1 get if possible
# iteration 2 compute the number of mutations

from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque()
        q.append((0, startGene))
        visited = {}
        bank.append(endGene)
        bank.append(startGene)
        if endGene not in bank: return -1

        while len(q) > 0:
            level, current = q.popleft()
            visited[current] = True

            if current == endGene:
                return level

            # Navigate mutations
            for i, g in enumerate(current):
                for changed in ['A', 'C', 'G', 'T']:
                    mut = current[:i] + changed + current[i + 1:]
                    if mut in bank and mut not in visited:
                        q.append((level + 1, mut))

        return -1



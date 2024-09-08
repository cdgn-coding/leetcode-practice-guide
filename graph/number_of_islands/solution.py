import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        queue = collections.deque()
        islands = 0

        rows = len(grid)
        cols = len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # Do nothing else
                if grid[row][col] == '0':
                    continue

                if (row, col) in visited:
                    continue

                # We found not visited ground, it is a new island
                islands += 1

                queue.append((row, col))
                while queue:
                    i, j = queue.popleft()
                    if grid[i][j] == '1' and (i, j) not in visited:
                        visited.add((i, j))
                        # right cell
                        if i < rows - 1: queue.append((i + 1, j))
                        # left cell
                        if i > 0: queue.append((i - 1, j))
                        # down cell
                        if j < cols - 1: queue.append((i, j + 1))
                        # upper cell
                        if j > 0: queue.append((i, j - 1))

        return islands
"""
DFS graph with circles

    1    ----> (n - 1, 0    )
    n^2  ----> (0    , 0    )

    From now on use n = n - 1 (0 indexed positions for the sake of clarity of formulas)
    Be i the current cell

    (i // n) % 2 == 0 -----> left to right
    (i // n) % 2 == 1 -----> right to left

    Be row the current row in the board for cell i
    row = n - i // n

    Be col the current column in the board for cell i
    rtl = (i // n) % 2
    col = n * (rtl) + (-1)^rtl * (i % n)

    Each game state has a current position and moves done before
"""
import collections
from math import inf
from typing import List, Dict, Tuple


class Solution:
    def generatePositions(self, n: int) -> Dict:
        row = n - 1
        col = 0
        pos = {}
        ltr = True
        for curr in range(1, n ** 2 + 1):
            pos[curr] = (row, col)
            if curr % n == 0:
                ltr = not ltr
                row -= 1
            else:
                col = col + 1 if ltr else col - 1
        return pos

    def position(self, n, i):
        positions = self.generatePositions(n)
        return positions[i]

    def visit(self, matrix, pos):
        x, y = self.position(len(matrix), pos)
        return matrix[x][y]

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        nsqrd = n ** 2
        root = (1, 0)
        visited = set()
        q = collections.deque()
        q.append(root)
        while q:
            curr, prev = q.popleft()

            # Prevent cycles
            if curr in visited:
                continue
            visited.add(curr)

            # If final position reached, count minimum if possible
            if curr == nsqrd:
                return prev

            # Traverse next moves
            for dice in range(1,7):
                _next = curr + dice
                if _next > nsqrd:
                    break
                if self.visit(board, _next) != -1:
                    q.append((self.visit(board, _next), prev + 1))
                else:
                    q.append((_next, prev + 1))

        return -1

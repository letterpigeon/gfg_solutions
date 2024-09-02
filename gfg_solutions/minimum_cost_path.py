"""
Given a square grid of size N, each cell of which contains an integer cost that represents a cost to traverse through that cell, we need to find a path from the top left cell to the bottom right cell by which the total cost incurred is minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j).

Examples :

Input: grid = {{9,4,9,9},{6,7,6,4},{8,3,3,7},{7,4,9,10}}
Output: 43
Explanation: The grid is-
9 4 9 9
6 7 6 4
8 3 3 7
7 4 9 10
The minimum cost is-
9 + 4 + 7 + 3 + 3 + 7 + 10 = 43.
Input: grid = {{4,4},{3,7}}
Output: 14
Explanation: The grid is-
4 4
3 7
The minimum cost is- 4 + 3 + 7 = 14.
Expected Time Complexity: O(n2*log(n))
Expected Auxiliary Space: O(n2)
 Constraints:
1 ≤ n ≤ 500
1 ≤ cost of cells ≤ 500
"""
import heapq
import unittest


class MinimumCostPath:
    """
    Need to use Dijkstra's algorithm to solve this problem.
    Doing a simple DP like below will not work as we can move in all 4 directions.  It might be possible that we move
    left or up to reach the destination with minimum cost.
    """

    def min_cost(self, grid):
        n = len(grid)
        dp = [[float('inf')] * n for _ in range(n)]
        dp[0][0] = grid[0][0]
        heap = [(dp[0][0], 0, 0)]
        while heap:
            cost, i, j = heapq.heappop(heap)
            if i == n - 1 and j == n - 1:
                return cost
            for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                if 0 <= x < n and 0 <= y < n:
                    new_cost = cost + grid[x][y]
                    if new_cost < dp[x][y]:
                        dp[x][y] = new_cost
                        heapq.heappush(heap, (new_cost, x, y))
        return -1


class TestMinimumCostPath(unittest.TestCase):
    def test_single_cell_grid(self):
        grid = [[5]]
        mcp = MinimumCostPath()
        self.assertEqual(mcp.min_cost(grid), 5)

    def test_two_by_two_grid(self):
        grid = [[4, 4], [3, 7]]
        mcp = MinimumCostPath()
        self.assertEqual(mcp.min_cost(grid), 14)

    def test_three_by_three_grid(self):
        grid = [[1, 2, 3], [4, 8, 2], [1, 5, 3]]
        mcp = MinimumCostPath()
        self.assertEqual(mcp.min_cost(grid), 11)

    def test_four_by_four_grid(self):
        grid = [[9, 4, 9, 9], [6, 7, 6, 4], [8, 3, 3, 7], [7, 4, 9, 10]]
        mcp = MinimumCostPath()
        self.assertEqual(mcp.min_cost(grid), 43)

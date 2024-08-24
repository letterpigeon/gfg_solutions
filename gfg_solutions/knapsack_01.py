"""
You are given weights and values of items, and put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
In other words, given two integer arrays val and wt which represent values and weights associated with items respectively. Also given an integer W which represents knapsack capacity, find out the maximum sum values subset of val[] such that the sum of the weights of the corresponding subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don't pick it (0-1 property).

Examples :

Input: W = 4, val[] = {1,2,3}, wt[] = {4,5,1}
Output: 3
Explanation: Choose the last item that weighs 1 unit and holds a value of 3.
Input: W = 3, val[] = {1,2,3}, wt[] = {4,5,6}
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).
Expected Time Complexity: O(N*W).
Expected Auxiliary Space: O(N*W)

Constraints:
2 ≤ N ≤ 1000
1 ≤ W ≤ 1000
1 ≤ wt[i] ≤ 1000
1 ≤ val[i] ≤ 1000
"""


class Knapsack0_1:
    def knapsack(self, W, wt, val, n):
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                if wt[i - 1] <= w:
                    pick_i = dp[i - 1][w - wt[i - 1]] + val[i - 1]
                    skip_i = dp[i - 1][w]
                    dp[i][w] = max(pick_i, skip_i)
                else:
                    dp[i][w] = dp[i - 1][w]
        return dp[n][W]

import unittest

class TestKnapsack0_1(unittest.TestCase):
    def test_max_value_within_capacity(self):
        knapsack = Knapsack0_1()
        self.assertEqual(knapsack.knapsack(4, [4, 5, 1], [1, 2, 3], 3), 3)

    def test_no_items_fit(self):
        knapsack = Knapsack0_1()
        self.assertEqual(knapsack.knapsack(3, [4, 5, 6], [1, 2, 3], 3), 0)

    def test_all_items_fit(self):
        knapsack = Knapsack0_1()
        self.assertEqual(knapsack.knapsack(10, [1, 2, 3], [10, 20, 30], 3), 60)

    def test_some_items_fit(self):
        knapsack = Knapsack0_1()
        self.assertEqual(knapsack.knapsack(5, [1, 2, 3], [10, 20, 30], 3), 50)

    def test_zero_capacity(self):
        knapsack = Knapsack0_1()
        self.assertEqual(knapsack.knapsack(0, [1, 2, 3], [10, 20, 30], 3), 0)

    def test_empty_items(self):
        knapsack = Knapsack0_1()
        self.assertEqual(knapsack.knapsack(10, [], [], 0), 0)

if __name__ == '__main__':
    unittest.main()

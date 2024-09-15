"""
There are n stairs, and a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. Count the number of ways, the person can reach the top (order does not matter).
Note: Order does not matter means for n = 4:- {1 2 1},{2 1 1},{1 1 2} are considered same.

Examples :

Input: n = 4
Output: 3
Explanation: Three ways to reach at 4th stair. They are {1, 1, 1, 1}, {1, 1, 2}, {2, 2}.
Input: n = 5
Output: 3
Explanation: Three ways to reach at 5th stair. They are {1, 1, 1, 1, 1}, {1, 1, 2, 1} and {1, 2, 2}.
Expected Time Complexity: O(n)
Expected Space Complexity: O(n)

Constraints:
1 ≤ n ≤ 104
"""

class CountWaysToNthStairs:
    def count_ways(self, n):
        return n // 2 + 1

import unittest

class TestCountWaysToNthStairs(unittest.TestCase):
    def test_single_stair(self):
        cws = CountWaysToNthStairs()
        self.assertEqual(cws.count_ways(1), 1)

    def test_two_stairs(self):
        cws = CountWaysToNthStairs()
        self.assertEqual(cws.count_ways(2), 2)

    def test_three_stairs(self):
        cws = CountWaysToNthStairs()
        self.assertEqual(cws.count_ways(3), 2)

    def test_four_stairs(self):
        cws = CountWaysToNthStairs()
        self.assertEqual(cws.count_ways(4), 3)

    def test_five_stairs(self):
        cws = CountWaysToNthStairs()
        self.assertEqual(cws.count_ways(5), 3)

    def test_six_stairs(self):
        cws = CountWaysToNthStairs()
        self.assertEqual(cws.count_ways(6), 4)

    def test_large_number_of_stairs(self):
        cws = CountWaysToNthStairs()
        self.assertEqual(cws.count_ways(10000), 5001)

    def test_zero_stairs(self):
        cws = CountWaysToNthStairs()
        self.assertEqual(cws.count_ways(0), 1)

    def test_large_odd_number_of_stairs(self):
        cws = CountWaysToNthStairs()
        self.assertEqual(cws.count_ways(9999), 5000)

if __name__ == '__main__':
    unittest.main()
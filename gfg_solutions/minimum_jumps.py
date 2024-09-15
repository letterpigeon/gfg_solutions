"""
Given an array arr[] of non-negative integers. Each array element represents the maximum length of the jumps that can be made forward from that element. This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
Find the minimum number of jumps to reach the end of the array starting from the first element. If an element is 0, then you cannot move through that element.
Note:  Return -1 if you can't reach the end of the array.

Examples :

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3
Explanation:First jump from 1st element to 2nd element with value 3. From here we jump to 5th element with value 9, and from here we will jump to the last.
Input: arr = {1, 4, 3, 2, 6, 7}
Output: 2
Explanation: First we jump from the 1st to 2nd element and then jump to the last element.
Input: arr = {0, 10, 20}
Output: -1
Explanation: We cannot go anywhere from the 1st element.
Expected Time Complexity: O(n)
Expected Space Complexity: O(1)

Constraints:
0 ≤ arr[i] ≤ 105
2 ≤ arr.size() ≤ 106
"""

class MininumJumps:
    def min_jumps(self, arr):
        n: int = len(arr)
        if n <= 1:
            return 0

        jumps: int = 0
        furthest: int = 0
        current_end: int = 0

        for i in range(n):
            furthest = max(furthest, i + arr[i])
            if i == current_end:
                jumps += 1
                current_end = furthest
                if current_end >= n - 1:
                    return jumps

            if furthest <= i:
                return -1

        return -1

import unittest

class TestMininumJumps(unittest.TestCase):
    def test_single_element(self):
        mj = MininumJumps()
        self.assertEqual(mj.min_jumps([0]), 0)

    def test_no_jumps_possible(self):
        mj = MininumJumps()
        self.assertEqual(mj.min_jumps([0, 1, 2]), -1)

    def test_minimum_jumps(self):
        mj = MininumJumps()
        self.assertEqual(mj.min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]), 3)

    def test_jump_to_last_element(self):
        mj = MininumJumps()
        self.assertEqual(mj.min_jumps([1, 4, 3, 2, 6, 7]), 2)

    def test_large_jump_at_start(self):
        mj = MininumJumps()
        self.assertEqual(mj.min_jumps([10, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 1)

    def test_all_zeros_except_first(self):
        mj = MininumJumps()
        self.assertEqual(mj.min_jumps([1, 0, 0, 0, 0]), -1)

    def test_large_array(self):
        mj = MininumJumps()
        self.assertEqual(mj.min_jumps([1] * 1000000), 999999)

    def test_alternating_large_small_jumps(self):
        mj = MininumJumps()
        self.assertEqual(mj.min_jumps([1, 10, 1, 10, 1, 10, 1, 10, 1, 10]), 2)

    def test_large_numbers(self):
        mj = MininumJumps()
        self.assertEqual(mj.min_jumps([100000, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 1)

    def test_end_reachable_with_exact_jumps(self):
        mj = MininumJumps()
        self.assertEqual(mj.min_jumps([2, 3, 1, 1, 4]), 2)
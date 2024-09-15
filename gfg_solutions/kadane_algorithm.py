"""
Given an integer array arr[]. Find the contiguous sub-array(containing at least one number) that has the maximum sum and return its sum.

Examples:

Input: arr[] = [1, 2, 3, -2, 5]
Output: 9
Explanation: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.
Input: arr[] = [-1, -2, -3, -4]
Output: -1
Explanation: Max subarray sum is -1 of element (-1)
Input: arr[] = [5, 4, 7]
Output: 16
Explanation: Max subarray sum is 16 of element (5, 4, 7)
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ arr.size() ≤ 105
-107 ≤ arr[i] ≤ 107
"""
import unittest

class KadaneAlgorithm:
    def max_subarray_sum(self, arr):
        max_sum = float('-inf')
        current_sum = 0
        for num in arr:
            current_sum += num
            max_sum = max(max_sum, current_sum)
            current_sum = max(current_sum, 0)
        return max_sum



class TestKadaneAlgorithm(unittest.TestCase):
    def test_positive_numbers(self):
        ka = KadaneAlgorithm()
        self.assertEqual(ka.max_subarray_sum([1, 2, 3, -2, 5]), 9)

    def test_all_negative_numbers(self):
        ka = KadaneAlgorithm()
        self.assertEqual(ka.max_subarray_sum([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        ka = KadaneAlgorithm()
        self.assertEqual(ka.max_subarray_sum([5, 4, -1, 7, 8]), 23)

    def test_single_element_positive(self):
        ka = KadaneAlgorithm()
        self.assertEqual(ka.max_subarray_sum([5]), 5)

    def test_single_element_negative(self):
        ka = KadaneAlgorithm()
        self.assertEqual(ka.max_subarray_sum([-5]), -5)

    def test_empty_array(self):
        ka = KadaneAlgorithm()
        self.assertEqual(ka.max_subarray_sum([]), float('-inf'))

    def test_large_numbers(self):
        ka = KadaneAlgorithm()
        self.assertEqual(ka.max_subarray_sum([10**7, -10**7, 10**7]), 10**7)

    def test_large_array(self):
        ka = KadaneAlgorithm()
        self.assertEqual(ka.max_subarray_sum([1] * 10**5), 10**5)

    def test_alternating_positive_negative(self):
        ka = KadaneAlgorithm()
        self.assertEqual(ka.max_subarray_sum([1, -1, 1, -1, 1]), 1)

    def test_all_zeros(self):
        ka = KadaneAlgorithm()
        self.assertEqual(ka.max_subarray_sum([0, 0, 0, 0]), 0)

if __name__ == '__main__':
    unittest.main()
"""
Given two sorted arrays of distinct integers arr1 and arr2. Each array may have some elements in common with the other array. Find the maximum sum of a path from the beginning of any array to the end of any array. You can switch from one array to another array only at the common elements.

Note:  When we switch from one array to other,  we need to consider the common element only once in the result.

Examples :

Input: arr1 = [2, 3, 7, 10, 12] , arr2 = [1, 5, 7, 8]
Output: 35
Explanation: The path will be 1+5+7+10+12 = 35, where 1 and 5 come from arr2 and then 7 is common so we switch to arr1 and add 10 and 12.
Input: arr1 = [1, 2, 3] , arr2[] = [3, 4, 5]
Output: 15
Explanation: The path will be 1+2+3+4+5=15.
Expected Time Complexity: O(m + n)
Expected Auxiliary Space: O(1)
Constraints:
1 <= arr1.size(), arr2.size() <= 104
1 <= arr1[i], arr2[i] <= 105
"""

import unittest

class MaxSumPath:
    def max_path_sum(self, arr1, arr2):
        result, sum1, sum2 = 0, 0, 0
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                sum1 += arr1[i]
                i += 1
            elif arr1[i] > arr2[j]:
                sum2 += arr2[j]
                j += 1
            else:
                result += max(sum1, sum2) + arr1[i]
                sum1, sum2 = 0, 0
                i += 1
                j += 1
        sum1 += sum(arr1[i:])
        sum2 += sum(arr2[j:])
        result += max(sum1, sum2)
        return result



class TestMaxSumPath(unittest.TestCase):
    def test_no_common_elements(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        msp = MaxSumPath()
        self.assertEqual(msp.max_path_sum(arr1, arr2), 15)

    def test_all_common_elements(self):
        arr1 = [1, 2, 3]
        arr2 = [1, 2, 3]
        msp = MaxSumPath()
        self.assertEqual(msp.max_path_sum(arr1, arr2), 6)

    def test_single_element_arrays(self):
        arr1 = [1]
        arr2 = [2]
        msp = MaxSumPath()
        self.assertEqual(msp.max_path_sum(arr1, arr2), 2)

    def test_single_common_element(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 3, 4]
        msp = MaxSumPath()
        self.assertEqual(msp.max_path_sum(arr1, arr2), 10)

    def test_common_element_at_start(self):
        arr1 = [1, 4, 5]
        arr2 = [1, 2, 3]
        msp = MaxSumPath()
        self.assertEqual(msp.max_path_sum(arr1, arr2), 10)

    def test_common_element_at_end(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 3]
        msp = MaxSumPath()
        self.assertEqual(msp.max_path_sum(arr1, arr2), 12)

    def test_empty_first_array(self):
        arr1 = []
        arr2 = [1, 2, 3]
        msp = MaxSumPath()
        self.assertEqual(msp.max_path_sum(arr1, arr2), 6)

    def test_empty_second_array(self):
        arr1 = [1, 2, 3]
        arr2 = []
        msp = MaxSumPath()
        self.assertEqual(msp.max_path_sum(arr1, arr2), 6)

    def test_large_arrays(self):
        arr1 = list(range(1, 10001))
        arr2 = list(range(5000, 15001))
        msp = MaxSumPath()
        self.assertEqual(msp.max_path_sum(arr1, arr2), sum(range(1, 15001)))

    def test_alternating_common_elements(self):
        arr1 = [1, 3, 5, 7, 9]
        arr2 = [2, 3, 4, 7, 8]
        msp = MaxSumPath()
        self.assertEqual(msp.max_path_sum(arr1, arr2), 26)

if __name__ == '__main__':
    unittest.main()
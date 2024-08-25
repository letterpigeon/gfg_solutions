"""
Given two positive integer arrays arr and brr, find the number of pairs such that xy > yx (raised to power of) where x is an element from arr and y is an element from brr.

Examples :

Input: arr[] = [2, 1, 6], brr[] = [1, 5]
Output: 3
Explanation: The pairs which follow xy > yx are: 21 > 12,  25 > 52 and 61 > 16 .
Input: arr[] = [2 3 4 5], brr[] = [1 2 3]
Output: 5
Explanation: The pairs which follow xy > yx are: 21 > 12 , 31 > 13 , 32 > 23 , 41 > 14 , 51 > 15 .
Expected Time Complexity: O((N + M)log(N)).
Expected Auxiliary Space: O(1).

Constraints:
1 ≤ arr.size(), brr.size() ≤ 105
1 ≤ brr[i], arr[i] ≤ 103
"""
from typing import List
from bisect import bisect_right
import unittest


class NumberOfPairs:
    @staticmethod
    def count_pairs(arr: List[int], brr: List[int]) -> int:
        """
        if x = 1, then 1^y = 1 for all y, but y^1 = y for all y > 1, hence x^y > y^x is always false for x = 1
        if y = 1, then x^1 = x for all x, but 1^x = 1 for all x > 1, hence x^y > y^x is always true for x > 1
        if x = 2, y = 3, then 2^3 < 3^2. But for y=4, 2^4 = 4^2.  For y>4, 2^y > y^2.  y=3 and y=4 are the special
        cases that need to be excluded
        if x = 3, 3^1 > 1^3, 3^2 > 2^3, 3^3 = 3^3, 3^y > y^3 for all y > 3 (i.e y > x), hence y1 and y2 are the special
        case.  y2 needs to be added back.  y1 is already added for all y=1
        """
        arr.sort()
        brr.sort()

        count_y1 = brr.count(1)
        count_y2 = brr.count(2)
        count_y3 = brr.count(3)
        count_y4 = brr.count(4)

        def count_pairs_for_x(x):
            if x <= 1:
                return 0
            # look for the first element greater than x to count the number of elements in brr greater than x
            idx = bisect_right(brr, x)
            count = len(brr) - idx
            count += count_y1

            if x == 2:
                count -= (count_y3 + count_y4)
            if x == 3:
                count += count_y2

            return count

        total_pairs = 0
        for x in arr:
            total_pairs += count_pairs_for_x(x)

        return total_pairs


class TestNumberOfPairs(unittest.TestCase):
    def test_pairs_with_no_elements(self):
        self.assertEqual(NumberOfPairs.count_pairs([], []), 0)

    def test_pairs_with_single_element(self):
        self.assertEqual(NumberOfPairs.count_pairs([2], [1]), 1)

    def test_pairs_with_multiple_elements(self):
        self.assertEqual(NumberOfPairs.count_pairs([2, 1, 6], [1, 5]), 3)

    def test_pairs_with_all_elements_equal(self):
        self.assertEqual(NumberOfPairs.count_pairs([2, 2, 2], [2, 2, 2]), 0)

    def test_pairs_with_large_numbers(self):
        self.assertEqual(NumberOfPairs.count_pairs([1000, 999], [998, 997]), 0)

    def test_pairs_with_mixed_elements(self):
        self.assertEqual(NumberOfPairs.count_pairs([2, 3, 4, 5], [1, 2, 3]), 5)

    def test_pairs_with_zero_elements(self):
        self.assertEqual(NumberOfPairs.count_pairs([0, 0, 0], [1, 2, 3]), 0)

    def test_pairs_with_one_in_brr(self):
        self.assertEqual(NumberOfPairs.count_pairs([2, 3, 4], [1, 1, 1]), 9)


if __name__ == '__main__':
    unittest.main()

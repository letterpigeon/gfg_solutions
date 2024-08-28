"""
Given an array of integers arr, sort the array according to the frequency of elements, i.e. elements that have higher frequency comes first. If the frequencies of two elements are the same, then the smaller number comes first.

Examples :

Input: arr[] = [5, 5, 4, 6, 4]
Output: [4, 4, 5, 5, 6]
Explanation: The highest frequency here is 2. Both 5 and 4 have that frequency. Now since the frequencies are the same the smaller element comes first. So 4 4 comes first then comes 5 5. Finally comes 6. The output is 4 4 5 5 6.
Input: arr[] = [9, 9, 9, 2, 5]
Output: [9, 9, 9, 2, 5]
Explanation: The highest frequency here is 3. Element 9 has the highest frequency So 9 9 9 comes first. Now both 2 and 5 have the same frequency. So we print smaller elements first. The output is 9 9 9 2 5.
Expected Time Complexity: O(n*logn)
Expected Space Complexity: O(n)

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i]≤ 105
"""
from collections import Counter
import unittest

class SortByFrequence:
    def sort_by_frequency(self, arr):
        histogram = Counter(arr)
        return sorted(arr, key=lambda x: (-histogram.get(x), x))

class TestSortByFrequence(unittest.TestCase):
    def test_empty_array(self):
        sorter = SortByFrequence()
        self.assertEqual(sorter.sort_by_frequency([]), [])

    def test_single_element_array(self):
        sorter = SortByFrequence()
        self.assertEqual(sorter.sort_by_frequency([1]), [1])

    def test_multiple_elements_with_same_frequency(self):
        sorter = SortByFrequence()
        self.assertEqual(sorter.sort_by_frequency([5, 5, 4, 6, 4]), [4, 4, 5, 5, 6])

    def test_all_elements_same(self):
        sorter = SortByFrequence()
        self.assertEqual(sorter.sort_by_frequency([9, 9, 9, 9]), [9, 9, 9, 9])

    def test_elements_with_different_frequencies(self):
        sorter = SortByFrequence()
        self.assertEqual(sorter.sort_by_frequency([9, 9, 9, 2, 5]), [9, 9, 9, 2, 5])

    def test_elements_with_same_frequency_and_different_values(self):
        sorter = SortByFrequence()
        self.assertEqual(sorter.sort_by_frequency([3, 1, 2, 2, 1, 3]), [1, 1, 2, 2, 3, 3])

    def test_large_numbers(self):
        sorter = SortByFrequence()
        self.assertEqual(sorter.sort_by_frequency([100000, 100000, 99999]), [100000, 100000, 99999])

    def test_negative_numbers(self):
        sorter = SortByFrequence()
        self.assertEqual(sorter.sort_by_frequency([-1, -2, -2, -1, -3]), [-2, -2, -1, -1, -3])

if __name__ == '__main__':
    unittest.main()
"""
Given a positive integer n. You have to find nth natural number after removing all the numbers containing the digit 9.

Examples :

Input: n = 8
Output: 8
Explanation: After removing natural numbers which contains digit 9, first 8 numbers are 1,2,3,4,5,6,7,8 and 8th number is 8.
Input: n = 9
Output: 10
Explanation: After removing natural numbers which contains digit 9, first 9 numbers are 1,2,3,4,5,6,7,8,10 and 9th number is 10.
Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)
"""

import unittest

class NthNaturalNumber:
    def find_natural_number(self, n):
        result = 0
        power = 1
        while n:
            result += power * (n % 9)
            n //= 9
            power *= 10
        return result


class TestNthNaturalNumber(unittest.TestCase):
    def test_first_natural_number(self):
        nnn = NthNaturalNumber()
        self.assertEqual(nnn.find_natural_number(1), 1)

    def test_eighth_natural_number(self):
        nnn = NthNaturalNumber()
        self.assertEqual(nnn.find_natural_number(8), 8)

    def test_ninth_natural_number(self):
        nnn = NthNaturalNumber()
        self.assertEqual(nnn.find_natural_number(9), 10)

    def test_tenth_natural_number(self):
        nnn = NthNaturalNumber()
        self.assertEqual(nnn.find_natural_number(10), 11)

    def test_large_natural_number(self):
        nnn = NthNaturalNumber()
        self.assertEqual(nnn.find_natural_number(100), 121)

    def test_large_natural_number_with_multiple_nines(self):
        nnn = NthNaturalNumber()
        self.assertEqual(nnn.find_natural_number(81), 100)

    def test_zero_natural_number(self):
        nnn = NthNaturalNumber()
        self.assertEqual(nnn.find_natural_number(0), 0)

    def test_large_number(self):
        nnn = NthNaturalNumber()
        self.assertEqual(nnn.find_natural_number(1000), 1331)

    def test_number_with_leading_nine(self):
        nnn = NthNaturalNumber()
        self.assertEqual(nnn.find_natural_number(89), 108)

    def test_number_with_trailing_nine(self):
        nnn = NthNaturalNumber()
        self.assertEqual(nnn.find_natural_number(98), 118)

if __name__ == '__main__':
    unittest.main()

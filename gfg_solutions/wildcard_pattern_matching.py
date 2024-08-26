"""
Given two strings pattern and str which may be of different size, You have to return 1 if the wildcard pattern i.e. pattern, matches with str else return 0. All characters of the string str and pattern always belong to the Alphanumeric characters.

The wildcard pattern can include the characters ? and *
‘?’ – matches any single character.
‘*’ – Matches any sequence of characters (including the empty sequence).

Note: The matching should cover the entire str (not partial str).

Examples:

Input: pattern = "ba*a?", str = "baaabab"
Output: 1
Explanation: replace '*' with "aab" and
'?' with 'b'.
"""

class WildcardPatternMatching:
    def is_match(self, pattern: str, s: str) -> bool:
        m, n = len(pattern), len(s)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            if pattern[i -1] == '*':
                dp[i][0] = dp[i-1][0]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if pattern[i - 1] == s[j - 1] or pattern[i - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
                elif pattern[i - 1] == '*':
                    dp[i][j] = dp[i- 1][j] or dp[i][j -1]

        return dp[m][n]

import unittest

class TestWildcardPatternMatching(unittest.TestCase):
    def test_empty_pattern_and_string(self):
        matcher = WildcardPatternMatching()
        self.assertTrue(matcher.is_match("", ""))

    def test_empty_pattern_non_empty_string(self):
        matcher = WildcardPatternMatching()
        self.assertFalse(matcher.is_match("", "abc"))

    def test_non_empty_pattern_empty_string(self):
        matcher = WildcardPatternMatching()
        self.assertFalse(matcher.is_match("a*", ""))

    def test_exact_match(self):
        matcher = WildcardPatternMatching()
        self.assertTrue(matcher.is_match("abc", "abc"))

    def test_single_wildcard_match(self):
        matcher = WildcardPatternMatching()
        self.assertTrue(matcher.is_match("a?c", "abc"))

    def test_multiple_wildcards_match(self):
        matcher = WildcardPatternMatching()
        self.assertTrue(matcher.is_match("a*bc", "aXYZbc"))

    def test_wildcard_match_entire_string(self):
        matcher = WildcardPatternMatching()
        self.assertTrue(matcher.is_match("*", "anything"))

    def test_wildcard_match_empty_string(self):
        matcher = WildcardPatternMatching()
        self.assertTrue(matcher.is_match("*", ""))

    def test_wildcard_with_question_mark(self):
        matcher = WildcardPatternMatching()
        self.assertTrue(matcher.is_match("a*b?d", "aXYZbcd"))

    def test_no_match_different_lengths(self):
        matcher = WildcardPatternMatching()
        self.assertFalse(matcher.is_match("abc", "abcd"))

    def test_no_match_different_characters(self):
        matcher = WildcardPatternMatching()
        self.assertFalse(matcher.is_match("abc", "abd"))

    def test_no_match_with_wildcard(self):
        matcher = WildcardPatternMatching()
        self.assertFalse(matcher.is_match("a*c", "abd"))

if __name__ == '__main__':
    unittest.main()
"""
Given an array arr of lowercase strings, determine if the strings can be chained together to form a circle.
A string X can be chained together with another string Y if the last character of X is the same as the first character of Y. If every string of the array can be chained with exactly two strings of the array(one with the first character and the second with the last character of the string), it will form a circle.

For example, for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf"

Examples

Input: arr[] = ["abc", "bcd", "cdf"]
Output: 0
Explaination: These strings can't form a circle because no string has 'd'at the starting index.
Input: arr[] = ["ab" , "bc", "cd", "da"]
Output: 1
Explaination: These strings can form a circle of strings.
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(n)

Constraints:
1 ≤ length of strings ≤ 20
"""

from collections import defaultdict

class CircleOfStrings:
    def can_form_circle(self, arr):
        def dfs(graph, node, visited):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(graph, neighbor, visited)

        if not arr:
            return 0

        graph = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for word in arr:
            start, end = word[0], word[-1]
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1

        for node in graph:
            if in_degree[node] != out_degree[node]:
                return 0

        visited = {node: False for node in graph}
        start = arr[0][0]
        dfs(graph, start, visited)
        for node in visited:
            if not visited[node]:
                return 0
        return 1

import unittest

class TestCircleOfStrings(unittest.TestCase):
    def test_strings_form_circle(self):
        cos = CircleOfStrings()
        self.assertEqual(cos.can_form_circle(["ab", "bc", "cd", "da"]), 1)

    def test_strings_do_not_form_circle(self):
        cos = CircleOfStrings()
        self.assertEqual(cos.can_form_circle(["abc", "bcd", "cdf"]), 0)

    def test_single_string(self):
        cos = CircleOfStrings()
        self.assertEqual(cos.can_form_circle(["a"]), 1)

    def test_two_strings_form_circle(self):
        cos = CircleOfStrings()
        self.assertEqual(cos.can_form_circle(["ab", "ba"]), 1)

    def test_two_strings_do_not_form_circle(self):
        cos = CircleOfStrings()
        self.assertEqual(cos.can_form_circle(["ab", "cd"]), 0)

    def test_empty_list(self):
        cos = CircleOfStrings()
        self.assertEqual(cos.can_form_circle([]), 0)

    def test_strings_with_same_start_and_end(self):
        cos = CircleOfStrings()
        self.assertEqual(cos.can_form_circle(["aa", "aa", "aa"]), 1)

    def test_strings_with_different_lengths(self):
        cos = CircleOfStrings()
        self.assertEqual(cos.can_form_circle(["a", "b", "c", "d"]), 0)

    def test_strings_with_mixed_case(self):
        cos = CircleOfStrings()
        self.assertEqual(cos.can_form_circle(["Ab", "bC", "Cd", "dA"]), 1)

    def test_strings_with_special_characters(self):
        cos = CircleOfStrings()
        self.assertEqual(cos.can_form_circle(["a!", "!b", "b@", "@a"]), 1)